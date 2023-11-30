from django.shortcuts import render
from django.http import HttpResponse

from universities.models import UniversityModel
from students.models import StudentModel

def menu(request):
    menu_response = \
"""
<html>
    <head>
        <title>Menu</title>
    </head>
    <body>
        <h4>Django Lab Menu</h4>
        <a href="/populate/">Populate</a><br>
        <a href="/students/menu/">Students</a><br>
        <a href="/universities/menu/">Universities</a>
    </body>
</html>
"""
    return HttpResponse(menu_response)

def populate(request):
    uni1 = UniversityModel.objects.create(
        full_name='Новосибирский Государственный Университет',
        abbreviation_name='НГУ',
        founded_date='1958-01-09')
    uni2 = UniversityModel.objects.create(
        full_name='Massachusetts Institute of Technology',
        abbreviation_name='MIT',
        founded_date='1861-04-10')
    uni3 = UniversityModel.objects.create(
        full_name='Norwegian University of Science and Technology',
        abbreviation_name='NTNU',
        founded_date='1996-01-01')

    StudentModel.objects.create(full_name='Дементьева Анна Павловна',      university_id=uni1.id, admission_year=2008)
    StudentModel.objects.create(full_name='Авдеев Матвей Николаевич',      university_id=uni1.id, admission_year=1990)
    StudentModel.objects.create(full_name='Логинова Маргарита Данииловна', university_id=uni1.id, admission_year=1971)
    StudentModel.objects.create(full_name='Муратова Дарья Никитична',      university_id=uni1.id, admission_year=2005)
    StudentModel.objects.create(full_name='Фомин Антон Янович',            university_id=uni1.id, admission_year=1992)
    StudentModel.objects.create(full_name='Афанасьева Алиса Артёмовна',    university_id=uni1.id, admission_year=1970)
    StudentModel.objects.create(full_name='Орлова Алина Арсентьевна',      university_id=uni1.id, admission_year=2004)
    StudentModel.objects.create(full_name='Белоусов Илья Иванович',        university_id=uni1.id, admission_year=1993)
    StudentModel.objects.create(full_name='Орлова Милана Артёмовна',       university_id=uni1.id, admission_year=1982)
    StudentModel.objects.create(full_name='Баранова Стефания Марковна',    university_id=uni1.id, admission_year=1971)
    StudentModel.objects.create(full_name='Thomas Beaumont Rey',           university_id=uni2.id, admission_year=1977)
    StudentModel.objects.create(full_name='Kirsten Lorna Waters',          university_id=uni2.id, admission_year=2013)
    StudentModel.objects.create(full_name='Tracie Sharyn Danielson',       university_id=uni2.id, admission_year=1989)
    StudentModel.objects.create(full_name='Boyd Luanne Armstrong',         university_id=uni2.id, admission_year=2001)
    StudentModel.objects.create(full_name='Fancy Catharine Cummings',      university_id=uni2.id, admission_year=1977)
    StudentModel.objects.create(full_name='Violet Regan Dodge',            university_id=uni2.id, admission_year=1992)
    StudentModel.objects.create(full_name='Gae Seward Adams',              university_id=uni2.id, admission_year=1970)
    StudentModel.objects.create(full_name='Roseanne Careen Adcock',        university_id=uni2.id, admission_year=1984)
    StudentModel.objects.create(full_name='Maude Marilou Ash',             university_id=uni2.id, admission_year=1991)
    StudentModel.objects.create(full_name='Harriett Maree Butcher',        university_id=uni2.id, admission_year=1998)
    StudentModel.objects.create(full_name='Eleonor Malte Lennartsson',     university_id=uni3.id, admission_year=1996)
    StudentModel.objects.create(full_name='Peter Kathrine Van Schoorl',    university_id=uni3.id, admission_year=2010)
    StudentModel.objects.create(full_name='Milla Rigmor Haak',             university_id=uni3.id, admission_year=2004)
    StudentModel.objects.create(full_name='Jolanda Vilgot Wolff',          university_id=uni3.id, admission_year=1991)
    StudentModel.objects.create(full_name='Martine Vebjørn Olson',         university_id=uni3.id, admission_year=2011)
    StudentModel.objects.create(full_name='Lisa Lucia Alfons',             university_id=uni3.id, admission_year=2021)
    StudentModel.objects.create(full_name='Anna Thore Ananias',            university_id=uni3.id, admission_year=2008)
    StudentModel.objects.create(full_name='Tygo Rebekka Visser',           university_id=uni3.id, admission_year=2023)
    StudentModel.objects.create(full_name='Andreas Niek Holmberg',         university_id=uni3.id, admission_year=1999)
    StudentModel.objects.create(full_name='Torbjørn Signe Jakobsen',       university_id=uni3.id, admission_year=2013)

    response = """
<html>
    <head>
        <title>Populate</title>
    </head>
    <body>
        <p>Populated!</p>
        <a href="/menu/">Back to menu</a>
    </body>
</html>
"""

    return HttpResponse(response)
