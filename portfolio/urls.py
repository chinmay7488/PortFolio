from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("about/", views.AboutPage, name="AboutPage"),
    path("project/", views.ProjectPage, name="ProjectPage"),
    path("resume/", views.ResumePage, name="ResumePage")
] 