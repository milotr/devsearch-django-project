from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects,
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        'projectObj' : projectObj,
    }
    return render(request, 'projects/single-projects.html', context)

def createProject(request):
    form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'projects/project_form.html', context)