from django.urls import path
from . import views

urlpatterns = [
	path("",        views.universities_menu,   name="universities-menu"),
	path("menu/",   views.universities_menu,   name="universities-menu"),
	path("create/", views.universities_create, name="universities-create"),
	path("read/",   views.universities_read,   name="universities-read"),
	path("update/", views.universities_update, name="universities-update"),
	path("delete/", views.universities_delete, name="universities-delete")
]