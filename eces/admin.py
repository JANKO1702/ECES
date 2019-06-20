from django.contrib import admin
from .models import Etudiant
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group

# Register your models here.
admin.site.register(Etudiant)
admin.site.unregister(User)
admin.site.unregister(Group)
