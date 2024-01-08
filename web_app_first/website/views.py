from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_required, current_user
from .models import Habit
from . import db
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
views=Blueprint("views",__name__)

@views.route('/home', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        habit_name = request.form.get('habitName')
        category = request.form.get('category')
        type = request.form.get('type')
        custom_category = request.form.get('customCategory', '')
        
        if not habit_name:
            flash('You must enter a habit name', category='error')
            return render_template("home.html", user = current_user)
        if not category:
            flash('You must choose a category', category='error')
            return render_template("home.html", user = current_user)
        if not type:
            flash('You must choose a type', category='error')
            return render_template("home.html", user = current_user)

        if type in ['weekly', 'ocasional']:
            start_datetime_str, end_datetime_str = request.form.get('dateTimeRange').split(' to ')
            start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d %H:%M")
            
            new_habit = Habit(
            habit_name=habit_name,
            category=category,
            type=type,
            custom_category=custom_category,
            start_date=start_datetime.date(),
            end_date=end_datetime.date(),
            start_time=start_datetime.time(),
            end_time=end_datetime.time(),
            user_id=current_user.id
        )
        if type == 'daily':
            start_time_str, end_time_str = request.form.get('time_interval', '').split('-')
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
            print(start_time, end_time)
            new_habit = Habit(
            habit_name=habit_name,
            category=category,
            type=type,
            custom_category=custom_category,
            start_date=datetime.now().date(),
            end_date=None,
            start_time=start_time,
            end_time=end_time,
            user_id=current_user.id
        )
            

        
        db.session.add(new_habit)
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)

        return redirect(url_for('views.calendar'))
        
    return render_template("home.html", user = current_user)

    
@views.route('/calendar')
@login_required
def calendar():

    habits_today = Habit.query.filter_by(user_id=current_user.id, start_date=datetime.now().date()).order_by(Habit.start_time).all()
    return render_template("calendar.html", user=current_user, habits_today=habits_today)


@views.route('/stats')
@login_required
def stats():
    habits_today = Habit.query.filter_by(user_id=current_user.id, start_date=datetime.now().date(), completed=True).all()

    categories = ['work', 'leisure', 'health', 'custom']
    category_counts = {category: 0 for category in categories}

    for habit in habits_today:
        category_counts[habit.category] += 1
    if len(habits_today)>0:
        total_habits = len(habits_today)
    else:
        total_habits=1
    percentages = [round(count / total_habits * 100, 2) for count in category_counts.values()]

    return render_template("stats.html", user=current_user, categories=categories, percentages=percentages)
    
@views.route('/')
def pagina():
    return render_template("home_unauth.html", user = current_user )

@views.route('/submit-completion', methods=['POST'])
@login_required
def submit_completion():
    if request.method == 'POST':
        habit_ids = request.form.getlist('habit_ids')
        for habit_id in habit_ids:
            habit = Habit.query.get(habit_id)
            if habit:
                habit.completed = True
                try:
                    db.session.commit()
                except SQLAlchemyError as e:
                    print(e)

        flash('Completion submitted successfully!', category='success')

    return redirect(url_for('views.calendar'))