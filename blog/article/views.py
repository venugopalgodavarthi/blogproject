import re
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from article.forms import articleform
from article.models import articlemodel, commments
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/authe/login')
def addarticle(request):
    form = articleform()
    if request.method == 'POST':
        form = articleform(request.POST)
        form.save()
        return redirect('/index')
    return render(request, 'addarticle.html', {'form': form})


@login_required(login_url='/authe/login')
def modifyarticle(request, pk):
    res = articlemodel.objects.get(id=pk)
    if request.method == 'POST':
        if str(request.user) in [str(res.author)]:
            user = articlemodel.objects.get(id=pk)
            user.title = request.POST['title']
            user.adesc = request.POST['adesc']
            user.save()
            return redirect('/index')
    return render(request, 'updatearticle.html', {'res': res})


@login_required(login_url='/authe/login')
def deletearticle(request, pk):
    res = articlemodel.objects.get(id=pk)
    if request.method == 'POST':
        if str(request.user) in [str(res.author)]:
            articlemodel.objects.get(id=pk).delete()
            commments.objects.filter(article_id=res.id).delete()
            return redirect('/index')
    return render(request, 'deleteconfrim.html', {'res': res})


@login_required(login_url='/authe/login')
def indexview(request):
    res = articlemodel.objects.all()
    return render(request, 'index.html', {'res': res})


@login_required(login_url='/authe/login')
def articleview(request, pk):
    auth = False
    res = articlemodel.objects.get(id=pk)
    com = commments.objects.filter(article=res.id)
    if str(request.user) == str(res.author):
        auth = True
    if request.method == "POST":
        comm = request.POST['comment']
        commments.objects.create(
            article_id=res.id, content=comm, comname=request.user)
        return redirect('/articleview/{}'.format(res.id))
    return render(request, 'article.html', {'res': res, 'com': com, 'auth': auth})
