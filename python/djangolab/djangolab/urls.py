from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("",          views.menu,      name="menu"),
    path("menu/",     views.menu,      name="menu"),
    path("populate/", views.populate,  name="populate"),
    path("admin/",    admin.site.urls, name="admin"),

    path("universities/", include("universities.urls")),
    path("students/",     include("students.urls"))
]
