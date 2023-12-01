from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class UniversityForm(FlaskForm):
    full_name = StringField("Full Name: ", validators=[DataRequired()])
    abbreviation_name = StringField("Abbreviation Name: ", validators=[DataRequired()])
    founded_date = DateField("Founded Date:", format="%Y-%m-%d", validators=[DataRequired()])
    submit = SubmitField("Submit")