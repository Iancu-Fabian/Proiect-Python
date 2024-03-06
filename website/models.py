from . import db
from flask_login import UserMixin

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    type = db.Column(db.String(50))      
    custom_category = db.Column(db.String(100)) 
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    start_time=db.Column(db.Time)
    end_time=db.Column(db.Time)
    completed=db.Column(db.Boolean, default=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    habits = db.relationship('Habit')