from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

from database.model import UniversityModel

def make_student_form():

    class StudentForm(FlaskForm):
        full_name = StringField("Full Name: ", validators=[DataRequired()])
        admission_year = IntegerField("Admission Year:", validators=[DataRequired()])
        submit = SubmitField("Submit")

    choices = [(uni.id, uni.abbreviation_name) for uni in UniversityModel.query.all()]
    StudentForm.university_id = SelectField("University: ", validators=[DataRequired()], choices=choices)
    return StudentForm()

    