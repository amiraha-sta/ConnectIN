from App.models import User
from App.database import db
from .auth import login_user



def get_all_users():
    return User.query.all()

def create_user(firstName, lastName, username, password):
    newuser = User(firstName=firstName, lastName=lastName, username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()