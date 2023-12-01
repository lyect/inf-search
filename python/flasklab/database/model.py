from database.database import db

class UserModel(db.Model):

    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class UniversityModel(db.Model):

    __tablename__ = "university_table"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    abbreviation_name = db.Column(db.String(255), nullable=False)
    founded_date = db.Column(db.DateTime(), nullable=False)

    students = db.relationship("StudentModel", backref="university", lazy=True)

    def __str__(self):
        return self.abbreviation_name

class StudentModel(db.Model):

    __tablename__ = "student_table"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey("university_table.id"))
    admission_year = db.Column(db.Integer, nullable=False)