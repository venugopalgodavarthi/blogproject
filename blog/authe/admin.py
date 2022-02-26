from django.contrib import admin
from authe.models import registermodel
# Register your models here.


class registeradmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name',
                    'password', 'email', 'phone', 'age', 'gender']


admin.site.register(registermodel, registeradmin)
