from django.shortcuts import render

from .models import Project, Tech

# Create your views here.

def projects_list(request):
    projects = Project.objects.all()

    return render(request,'projects/projects_list.html', {
        'pro': projects
    })