from django.shortcuts import render


def HomePage(request):
    return render (request, 'home.html')

def AboutPage(request):
    return render (request, 'about.html')

def ProjectPage(request):
    return render (request, 'project.html')

def ResumePage(request):
    return render (request, 'resume.html')