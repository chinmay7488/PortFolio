from django.contrib import admin
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage, name="HomePage"),
    path("about/", views.AboutPage, name="AboutPage"),
    path("project/", views.ProjectPage, name="ProjectPage"),
    path("resume/", views.ResumePage, name="ResumePage")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)