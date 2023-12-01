from flask import Flask

from database.database import db
from universities.universities import universities_blueprint
from students.students import students_blueprint

from database.model import UniversityModel, StudentModel

class MyApplication(Flask):

    def __init__(self, name, database_uri):
        super().__init__(name)

        self.config["SQLALCHEMY_DATABASE_URI"] = database_uri
        self.config["SECRET_KEY"] = "super_duper_mega_secret_key"

    def setup_database(self, db):
        db.init_app(self)

        with self.app_context():
            db.create_all()

my_application = MyApplication(__name__, db.getURI())
my_application.setup_database(db)

my_application.register_blueprint(universities_blueprint, url_prefix="/universities")
my_application.register_blueprint(students_blueprint, url_prefix="/students")

@my_application.route("/")
@my_application.route('/menu/')
def index(): 
    menu_response = \
"""
<html>
    <head>
        <title>Menu</title>
    </head>
    <body>
        <h4>Flask Lab Menu</h4>
        <a href="/populate/">Populate</a><br>
        <a href="/students/menu/">Students</a><br>
        <a href="/universities/menu/">Universities</a>
    </body>
</html>
"""
    return menu_response

@my_application.route("/populate/")
def populate():
    uni1 = UniversityModel(
        full_name='Новосибирский Государственный Университет',
        abbreviation_name='НГУ',
        founded_date='1958-01-09')
    uni2 = UniversityModel(
        full_name='Massachusetts Institute of Technology',
        abbreviation_name='MIT',
        founded_date='1861-04-10')
    uni3 = UniversityModel(
        full_name='Norwegian University of Science and Technology',
        abbreviation_name='NTNU',
        founded_date='1996-01-01')

    db.session.add(uni1)
    db.session.add(uni2)
    db.session.add(uni3)

    db.session.commit()

    db.session.refresh(uni1)
    db.session.refresh(uni2)
    db.session.refresh(uni3)

    db.session.add(StudentModel(full_name='Дементьева Анна Павловна',      university_id=uni1.id, admission_year=2008))
    db.session.add(StudentModel(full_name='Авдеев Матвей Николаевич',      university_id=uni1.id, admission_year=1990))
    db.session.add(StudentModel(full_name='Логинова Маргарита Данииловна', university_id=uni1.id, admission_year=1971))
    db.session.add(StudentModel(full_name='Муратова Дарья Никитична',      university_id=uni1.id, admission_year=2005))
    db.session.add(StudentModel(full_name='Фомин Антон Янович',            university_id=uni1.id, admission_year=1992))
    db.session.add(StudentModel(full_name='Афанасьева Алиса Артёмовна',    university_id=uni1.id, admission_year=1970))
    db.session.add(StudentModel(full_name='Орлова Алина Арсентьевна',      university_id=uni1.id, admission_year=2004))
    db.session.add(StudentModel(full_name='Белоусов Илья Иванович',        university_id=uni1.id, admission_year=1993))
    db.session.add(StudentModel(full_name='Орлова Милана Артёмовна',       university_id=uni1.id, admission_year=1982))
    db.session.add(StudentModel(full_name='Баранова Стефания Марковна',    university_id=uni1.id, admission_year=1971))
    db.session.add(StudentModel(full_name='Thomas Beaumont Rey',           university_id=uni2.id, admission_year=1977))
    db.session.add(StudentModel(full_name='Kirsten Lorna Waters',          university_id=uni2.id, admission_year=2013))
    db.session.add(StudentModel(full_name='Tracie Sharyn Danielson',       university_id=uni2.id, admission_year=1989))
    db.session.add(StudentModel(full_name='Boyd Luanne Armstrong',         university_id=uni2.id, admission_year=2001))
    db.session.add(StudentModel(full_name='Fancy Catharine Cummings',      university_id=uni2.id, admission_year=1977))
    db.session.add(StudentModel(full_name='Violet Regan Dodge',            university_id=uni2.id, admission_year=1992))
    db.session.add(StudentModel(full_name='Gae Seward Adams',              university_id=uni2.id, admission_year=1970))
    db.session.add(StudentModel(full_name='Roseanne Careen Adcock',        university_id=uni2.id, admission_year=1984))
    db.session.add(StudentModel(full_name='Maude Marilou Ash',             university_id=uni2.id, admission_year=1991))
    db.session.add(StudentModel(full_name='Harriett Maree Butcher',        university_id=uni2.id, admission_year=1998))
    db.session.add(StudentModel(full_name='Eleonor Malte Lennartsson',     university_id=uni3.id, admission_year=1996))
    db.session.add(StudentModel(full_name='Peter Kathrine Van Schoorl',    university_id=uni3.id, admission_year=2010))
    db.session.add(StudentModel(full_name='Milla Rigmor Haak',             university_id=uni3.id, admission_year=2004))
    db.session.add(StudentModel(full_name='Jolanda Vilgot Wolff',          university_id=uni3.id, admission_year=1991))
    db.session.add(StudentModel(full_name='Martine Vebjørn Olson',         university_id=uni3.id, admission_year=2011))
    db.session.add(StudentModel(full_name='Lisa Lucia Alfons',             university_id=uni3.id, admission_year=2021))
    db.session.add(StudentModel(full_name='Anna Thore Ananias',            university_id=uni3.id, admission_year=2008))
    db.session.add(StudentModel(full_name='Tygo Rebekka Visser',           university_id=uni3.id, admission_year=2023))
    db.session.add(StudentModel(full_name='Andreas Niek Holmberg',         university_id=uni3.id, admission_year=1999))
    db.session.add(StudentModel(full_name='Torbjørn Signe Jakobsen',       university_id=uni3.id, admission_year=2013))

    db.session.commit()

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

    return response

if __name__ == '__main__':
    my_application.run()