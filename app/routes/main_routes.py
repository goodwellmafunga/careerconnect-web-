from flask import Blueprint, render_template
from app.models import News, Course, Event
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    news = News.query.all()
    courses = Course.query.all()
    events = Event.query.all()
    return render_template('index.html', news=news, courses=courses, events=events)

@main.route('/news')
def news():
    news = News.query.all()
    return render_template('news.html', news=news)

@main.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@main.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
