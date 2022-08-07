from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    context = {
        'text': "Artem's link",
        'projects': projects
    }
    return render(request, 'home.html', context)