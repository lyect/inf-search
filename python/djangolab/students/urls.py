from django.urls import path
from . import views

urlpatterns = [
	path("",        views.students_menu,   name="students-menu"),
	path("menu/",   views.students_menu,   name="students-menu"),
	path("create/", views.students_create, name="students-create"),
	path("read/",   views.students_read,   name="students-read"),
	path("update/", views.students_update, name="students-update"),
	path("delete/", views.students_delete, name="students-delete")
]