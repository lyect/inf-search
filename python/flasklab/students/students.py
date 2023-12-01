from flask import Blueprint, render_template, request

from database.database import db
from database.model import StudentModel
from students.forms import make_student_form

import datetime

students_blueprint = Blueprint("students_blueprint", __name__, template_folder="templates")

@students_blueprint.route("/")
@students_blueprint.route("/menu/")
def menu():
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
	return menu_response

def students_form_full_name_is_valid(full_name):
    if 0 < len(full_name) <= 255:
        return True
    return False 

def students_form_admission_year_is_valid(admission_year):
    if 0 <= int(admission_year) <= datetime.date.today().year:
        return True
    return False

def students_create_update(request, template_name, mode, id_to_update):
    stud_full_name = request.form["full_name"]
    stud_university_id = request.form["university_id"]
    stud_admission_year = request.form["admission_year"]

    stud_full_name_is_valid = students_form_full_name_is_valid(stud_full_name)
    stud_admission_year_is_valid = students_form_admission_year_is_valid(stud_admission_year)

    if stud_full_name_is_valid and stud_admission_year_is_valid:
        if mode == "UPDATE":
            stud = StudentModel.query.filter_by(id=id_to_update).first()
            stud.full_name = stud_full_name
            stud.university_id = stud_university_id
            stud.admission_year = stud_admission_year
            db.session.commit()
        elif mode == "CREATE":
            stud = StudentModel(
                full_name=stud_full_name,
                university_id=stud_university_id,
                admission_year=stud_admission_year)
            db.session.add(stud)
            db.session.commit()
        
        return render_template(template_name, status="SUCCESS")
    else:
        if       stud_full_name_is_valid and not stud_admission_year_is_valid:
            return render_template(template_name, status="INVALID_ADMISSION_YEAR")
        elif not stud_full_name_is_valid and     stud_admission_year_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME")
        elif not stud_full_name_is_valid and not stud_admission_year_is_valid:
            return render_template(template_name, status="INVALID_FULL_NAME_AND_ADMISSION_YEAR")

@students_blueprint.route("/create/", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        return students_create_update(request, "students_create_submit.html", "CREATE", None)
    return render_template("students_create.html", form=make_student_form())

@students_blueprint.route("/read/")
def read():
    return render_template("students_read.html", items=StudentModel.query.all())

@students_blueprint.route("/update/", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        if "id_to_update" not in request.form:
            return render_template("students_update_submit.html", status="NOT_SELECTED")
        return students_create_update(request, "students_update_submit.html", "UPDATE", request.form["id_to_update"])
    return render_template("students_update.html", form=make_student_form(), items=StudentModel.query.all())

@students_blueprint.route("/delete/", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        if "ids_to_delete" not in request.form:
            return render_template("students_delete_submit.html", status="NOT_SELECTED")
        ids_to_delete = request.form.getlist("ids_to_delete")

        for uni_id in ids_to_delete:
            try:
                uni_to_delete = StudentModel.query.filter_by(id=uni_id).delete()
            except Exception as e:
                db.session.rollback()
                return render_template("students_delete_submit.html", status="ERROR")
        db.session.commit()
        return render_template("students_delete_submit.html", status="SUCCESS")
    return render_template("students_delete.html", items=StudentModel.query.all())

