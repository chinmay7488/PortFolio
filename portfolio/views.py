from django.shortcuts import render
from portfolio.models import Skill, Certificate


def HomePage(request):
    return render (request, 'home.html')

def AboutPage(request):
    queryset = Skill.objects.all().values()

    sorted_queryset = queryset.order_by('Skill_priority').reverse()
    #print(sorted_queryset[0])

    return render (request, 'about.html',{'Skills':sorted_queryset})

def ProjectPage(request):
    return render (request, 'project.html')

def ResumePage(request):
    return render (request, 'resume.html')