from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

import datetime

from . import forms
from . import models

def students_form_full_name_is_valid(full_name):
    if 0 < len(full_name) <= 255:
        return True
    return False 

def students_form_admission_year_is_valid(admission_year):
    if 0 <= int(admission_year) <= datetime.date.today().year:
        return True
    return False

def students_create_update(request, form_name, data, mode, id_to_update):
    stud_full_name = request.POST.get("full_name")
    stud_university = request.POST.get("university")
    stud_admission_year = request.POST.get("admission_year")

    stud_full_name_is_valid = students_form_full_name_is_valid(stud_full_name)
    stud_admission_year_is_valid = students_form_admission_year_is_valid(stud_admission_year)

    if stud_full_name_is_valid and stud_admission_year_is_valid:
        if mode == "UPDATE":
            models.StudentModel.objects.filter(id=id_to_update).update(
                full_name=stud_full_name,
                university_id=stud_university,
                admission_year=stud_admission_year)
        elif mode == "CREATE":
            models.StudentModel.objects.create(
                full_name=stud_full_name,
                university_id=stud_university,
                admission_year=stud_admission_year)
        
        data["status"] = "SUCCESS"
        data[form_name] = forms.StudentsCreateForm()
    else:
        partially_filled_form_initial = dict()

        if       stud_full_name_is_valid and not stud_admission_year_is_valid:
            partially_filled_form_initial["full_name"] = stud_full_name
            data["status"] = "INVALID_ADMISSION_YEAR"
        elif not stud_full_name_is_valid and     stud_admission_year_is_valid:
            partially_filled_form_initial["admission_year"] = stud_admission_year
            data["status"] = "INVALID_FULL_NAME"
        elif not stud_full_name_is_valid and not stud_admission_year_is_valid:
            data["status"] = "INVALID_FULL_NAME_AND_ADMISSION_YEAR"

        data[form_name] = forms.StudentsCreateForm(
            initial=partially_filled_form_initial)

def students_menu(request):
    menu_response = \
"""
<html>
    <head>
        <title>Students</title>
    </head>
    <body>
        <h4>Students Table Menu</h4>
        <a href="/students/create/">Create</a><br>
        <a href="/students/read/">Read</a><br>
        <a href="/students/update/">Update</a><br>
        <a href="/students/delete/">Delete</a><br>
        <p>
            <a href="/menu/">Back to menu</a>
        </p>
    </body>
</html>
"""
    return HttpResponse(menu_response)
    
def students_create(request):
    data = dict()
    if request.method == "POST":
        students_create_update(request, "students_create_form", data, "CREATE", None)
    else:
        data["students_create_form"] = forms.StudentsCreateForm()
    
    return TemplateResponse(request, "students_create_template.html", data)

def students_read(request):

    data = {
        "values": models.StudentModel.objects.all()
    }

    return TemplateResponse(request, "students_read_template.html", data)

def students_update(request):
    data = dict()
    if request.method == "POST":
        id_to_update = request.POST.get("id_to_update")
        if id_to_update is None:
            data["status"] = "NOT_SELECTED"
            data["students_update_form"] = forms.StudentsCreateForm()
        else:
            students_create_update(request, "students_update_form", data, "UPDATE", id_to_update)
    else:
        data["students_update_form"] = forms.StudentsCreateForm()

    data["values"] = models.StudentModel.objects.all()

    return TemplateResponse(request, "students_update_template.html", data)

def students_delete(request):
    data = dict()
    if request.method == "POST":
        ids_to_delete = request.POST.getlist("ids_to_delete")
        if ids_to_delete is not None:
            for stud_id in ids_to_delete:
                try:
                    models.StudentModel.objects.filter(id=stud_id).delete()
                    data["status"] = "SUCCESS"
                except ProtectedError:
                    data["status"] = "ERROR"

    data["values"] = models.StudentModel.objects.all()

    return TemplateResponse(request, "students_delete_template.html", data)
