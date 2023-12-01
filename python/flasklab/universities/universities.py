from flask import Blueprint, render_template, request

from database.database import db
from database.model import UniversityModel
from universities.forms import UniversityForm

import datetime

universities_blueprint = Blueprint("universities_blueprint", __name__, template_folder="./templates")

@universities_blueprint.route("/")
@universities_blueprint.route("/menu/")
def menu():
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
    return menu_response

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

def universities_create_update(request, template_name, mode, id_to_update):
    uni_full_name = request.form["full_name"]
    uni_abbreviation_name = request.form["abbreviation_name"]
    uni_founded_date = request.form["founded_date"]

    uni_full_name_is_valid = universities_form_full_name_is_valid(uni_full_name)
    uni_abbreviation_name_is_valid = universities_form_abbreviation_name_is_valid(uni_abbreviation_name)
    uni_founded_date_is_valid = universities_form_founded_date_is_valid(uni_founded_date)

    if uni_full_name_is_valid and uni_abbreviation_name_is_valid and uni_founded_date_is_valid:
        if mode == "UPDATE":
            uni = UniversityModel.query.filter_by(id=id_to_update).first()
            uni.full_name = uni_full_name
            uni.abbreviation_name = uni_abbreviation_name
            uni.founded_date = uni_founded_date
            db.session.commit()
        elif mode == "CREATE":
            uni = UniversityModel(
                full_name=uni_full_name,
                abbreviation_name=uni_abbreviation_name,
                founded_date=uni_founded_date)
            db.session.add(uni)
            db.session.commit()

        return render_template(template_name, status="SUCCESS")
    else:
        if     uni_full_name_is_valid and     uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_FOUNDED_DATE")
        if     uni_full_name_is_valid and not uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_ABBREVIATION_NAME")
        if     uni_full_name_is_valid and not uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_ABBREVIATION_NAME_AND_FOUNDED_DATE")
        if not uni_full_name_is_valid and     uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME")
        if not uni_full_name_is_valid and     uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME_AND_FOUNDED_DATE")
        if not uni_full_name_is_valid and not uni_abbreviation_name_is_valid and     uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME_AND_ABBREVIATION_NAME")
        if not uni_full_name_is_valid and not uni_abbreviation_name_is_valid and not uni_founded_date_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME_AND_ABBREVIATION_NAME_AND_FOUNDED_DATE")

@universities_blueprint.route("/create/", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        return universities_create_update(request, "universities_create_submit.html", "CREATE", None)
    return render_template("universities_create.html", form=UniversityForm())

@universities_blueprint.route("/read/")
def read():
    return render_template("universities_read.html", items=UniversityModel.query.all())

@universities_blueprint.route("/update/", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        if "id_to_update" not in request.form:
            return render_template("universities_update_submit.html", status="NOT_SELECTED")
        return universities_create_update(request, "universities_update_submit.html", "UPDATE", request.form["id_to_update"])
    return render_template("universities_update.html", form=UniversityForm(), items=UniversityModel.query.all())

@universities_blueprint.route("/delete/", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        if "ids_to_delete" not in request.form:
            return render_template("universities_delete_submit.html", status="NOT_SELECTED")
        ids_to_delete = request.form.getlist("ids_to_delete")

        for uni_id in ids_to_delete:
            try:
                uni_to_delete = UniversityModel.query.filter_by(id=uni_id).delete()
            except Exception as e:
                db.session.rollback()
                return render_template("universities_delete_submit.html", status="ERROR")
        db.session.commit()
        return render_template("universities_delete_submit.html", status="SUCCESS")
    return render_template("universities_delete.html", items=UniversityModel.query.all())
