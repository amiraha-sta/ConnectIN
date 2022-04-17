from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from App.controllers import user, auth
from flask_login import login_required, current_user

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = auth.authenticate(request.form["email"], request.form["password"])
        if user:
            auth.login_user(user, False)
            return redirect('https://8080-amiraha-connectin-snq80gsoo8u.ws-us40.gitpod.io/profile')
        else:
            return ("Login Failed")
    else:
        return render_template('login.html')

@api_views.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == "POST":
        user.create_user(request.form["fname"], request.form["lname"], request.form["email"], request.form["password"] )
        return ("Signed in")
    else:
        return render_template('signUp.html')

@api_views.route('/profile', methods=['GET'])
@login_required
def profile():
    return ("Welcome " + current_user.firstName)

@api_views.route('/create-profile', methods=['GET'])
def createProfile():
    return render_template('createProfile.html')