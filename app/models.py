from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class register(db.Model):
    email = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    password2 = db.Column(db.String(128), nullable=False)
    alert = db.Column(db.String(128), nullable=False)
    message = db.Column(db.String(128), nullable=False)
    datebirth = db.Column(db.String(128), nullable=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')    


    def __repr__(self):
        return '<register {}>'.format(self.name)


class signin(db.Model):
    email1 =db.Column(db.String(128), primary_key=True)
    paskey = db.Column(db.String(128), nullable=False)
    remember_me = db.Column(db.String(128), nullable=False)
    submit1 = db.Column(db.String(128), nullable=False)


    def validate_password(self, paskey):
        user = User.query.filter_by(paskey=paskey.data).first()
        if user is None:
            raise ValidationError('That is not correct')
            return check_password_hash(self.password_hash, paskey)   


    def __repr__(self):
        return '<signin {}>'.format(self.name)




