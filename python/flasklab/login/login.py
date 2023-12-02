from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from database.model import UserModel
from database.database import db

from login.forms import SignupForm, SigninForm

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
	return UserModel.query.get(user_id)

login_blueprint = Blueprint("login_blueprint", __name__, template_folder="./templates")

@login_blueprint.route("/signup/", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		user_exists = (UserModel.query.filter_by(email=request.form["email"]).count() == 1)

		if not user_exists:
			user = UserModel(
				email=request.form["email"],
				name=request.form["name"],
				password=request.form["password"]
			)

			db.session.add(user)
			db.session.commit()

			return render_template("login_signup_submit.html", status="SUCCESS")
		return render_template("login_signup_submit.html", status="USER_EXISTS")
	return render_template("login_signup.html", form=SignupForm())

@login_blueprint.route("/signin/", methods=["GET", "POST"])
def signin():
	if current_user.is_authenticated:
		return render_template("login_signin_submit.html", status="ALREADY_SIGNED_IN")
	if request.method == "POST":
		user_query = UserModel.query.filter_by(email=request.form["email"], password=request.form["password"])
		if user_query.count() != 1:
			return render_template("login_signin_submit.html", status="INVALID_CREDENTIALS")
		login_user(user_query.first())
		return render_template("login_signin_submit.html", status="SUCCESS")
	return render_template("login_signin.html", form=SigninForm())

@login_blueprint.route("/logout/")
@login_required
def logout():
	logout_user()
	return render_template("login_logout_submit.html")