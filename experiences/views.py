from django.shortcuts import render

from .models import Experience, TechnologySkill


# Create your views here.
def experiences_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experiences/experiences_list.html',{
    'exp' : experiences
    })