from flask import Blueprint, redirect, render_template, request, send_from_directory

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@api_views.route('/signUp', methods=['GET'])
def signUp():
    return render_template('signUp.html')

@api_views.route('/create-profile', methods=['GET'])
def createProfile():
    return render_template('createProfile.html')

@api_views.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')
	
# # would need to be update to /profile/{id}
@api_views.route('/profile', methods=['GET']) 
def profile():
    return render_template('profile-page.html')
