from django.contrib import admin

# Register your models here.
from .models import Project, Tech

admin.site.register(Project)
admin.site.register(Tech)

