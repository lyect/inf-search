from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db.models import ProtectedError

import datetime

from . import forms
from . import models

def universities_form_full_name_is_valid(full_name):
    if 0 < len(full_name) <= 255:
        return True
    return False 

def universities_form_abbreviation_name_is_valid(abbreviation_name):
    if 0 < len(abbreviation_name) <= 255:
        return True
    return False 

def universities_form_founded_date_is_valid(founded_date):
    try:
        datetime.date.fromisoformat(founded_date)
        return True
    except ValueError:
        return False

def universities_create_update(request, form_name, data, mode, id_to_update):
    uni_full_name = request.POST.get("full_name")
    uni_abbreviation_name = request.POST.get("abbreviation_name")
    uni_founded_date = request.POST.get("founded_date")

    uni_full_name_is_valid = universities_form_full_name_is_valid(uni_full_name)
    uni_abbreviation_name_is_valid = universities_form_abbreviation_name_is_valid(uni_abbreviation_name)
    uni_founded_date_is_valid = universities_form_founded_date_is_valid(uni_founded_date)

    if uni_full_name_is_valid and uni_abbreviation_name_is_valid and uni_founded_date_is_valid:
        if mode == "UPDATE":
            models.UniversityModel.objects.filter(id=id_to_update).update(
                full_name=uni_full_name,
                abbreviation_name=uni_abbreviation_name,
                founded_date=uni_founded_date)
        elif mode == "CREATE":
            models.UniversityModel.objects.create(
                full_name=uni_full_name,
                abbreviation_name=uni_abbreviation_name,
                founded_date=uni_founded_date)
        
        data["status"] = "SUCCESS"
        data[form_name] = forms.UniversitiesCreateForm()
    else:
        partially_filled_form_initial = dict()

        if     uni_full_name_is_valid and     uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            partially_filled_form_initial["full_name"] = uni_full_name
            partially_filled_form_initial["abbreviation_name"] = uni_abbreviation_name
            data["status"] = "INVALID_FOUNDED_DATE"
        if     uni_full_name_is_valid and not uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            partially_filled_form_initial["full_name"] = uni_full_name
            partially_filled_form_initial["founded_date"] = uni_founded_date
            data["status"] = "INVALID_ABBREVIATION_NAME"
        if     uni_full_name_is_valid and not uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            partially_filled_form_initial["full_name"] = uni_full_name
            data["status"] = "INVALID_ABBREVIATION_NAME_AND_FOUNDED_DATE"
        if not uni_full_name_is_valid and     uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            partially_filled_form_initial["abbreviation_name"] = uni_abbreviation_name
            partially_filled_form_initial["founded_date"] = uni_founded_date
            data["status"] = "INVALID_FULL_NAME"
        if not uni_full_name_is_valid and     uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            partially_filled_form_initial["abbreviation_name"] = uni_abbreviation_name
            data["status"] = "INVALID_FULL_NAME_AND_FOUNDED_DATE"
        if not uni_full_name_is_valid and not uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            partially_filled_form_initial["founded_date"] = uni_founded_date
            data["status"] = "INVALID_FULL_NAME_AND_ABBREVIATION_NAME"
        if not uni_full_name_is_valid and not uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            data["status"] = "INVALID_FULL_NAME_AND_ABBREVIATION_NAME_AND_FOUNDED_DATE"

        data["universities_update_form"] = forms.UniversitiesCreateForm(
            initial=partially_filled_form_initial)

def universities_menu(request):
    menu_response = \
"""
<html>
    <head>
        <title>Universities</title>
    </head>
    <body>
        <h4>Universities Table Menu</h4>
        <a href="/universities/create/">Create</a><br>
        <a href="/universities/read/">Read</a><br>
        <a href="/universities/update/">Update</a><br>
        <a href="/universities/delete/">Delete</a><br>
        <p>
            <a href="/menu/">Back to menu</a>
        </p>
    </body>
</html>
"""
    return HttpResponse(menu_response)

def universities_create(request):
    data = dict()
    if request.method == "POST":
        universities_create_update(request, "universities_create_form", data, "CREATE", None)
    else:
        data["universities_create_form"] = forms.UniversitiesCreateForm()
    
    return TemplateResponse(request, "universities_create_template.html", data)

def universities_read(request):
    data = {
        "values": models.UniversityModel.objects.all()
    }

    return TemplateResponse(request, "universities_read_template.html", data)

def universities_update(request):
    data = dict()
    if request.method == "POST":
        id_to_update = request.POST.get("id_to_update")
        if id_to_update is None:
            data["status"] = "NOT_SELECTED"
            data["universities_update_form"] = forms.UniversitiesCreateForm()
        else:
            universities_create_update(request, "universities_update_form", data, "UPDATE", id_to_update)
    else:
        data["universities_update_form"] = forms.UniversitiesCreateForm()

    data["values"] = models.UniversityModel.objects.all()

    return TemplateResponse(request, "universities_update_template.html", data)

def universities_delete(request):
    data = dict()
    if request.method == "POST":
        ids_to_delete = request.POST.getlist("ids_to_delete")
        if ids_to_delete is not None:
            for uni_id in ids_to_delete:
                try:
                    models.UniversityModel.objects.filter(id=uni_id).delete()
                    data["status"] = "SUCCESS"
                except ProtectedError:
                    data["status"] = "ERROR"

    data["values"] = models.UniversityModel.objects.all()

    return TemplateResponse(request, "universities_delete_template.html", data)
