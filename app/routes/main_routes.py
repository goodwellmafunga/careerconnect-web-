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
    courses = [
        {"title": "Human Resources Management", "description": "Learn the skills to manage human resources in various organisations."},
        {"title": "Marketing Management", "description": "Develop strategies for effective marketing and business growth."},
        {"title": "Financial Accounting", "description": "Understand financial statements and the principles of accounting."},
        {"title": "Public Relations", "description": "Master the art of managing public perception and communication."},
        {"title": "Purchasing and Materials Management", "description": "Learn procurement and supply chain management techniques."},
        {"title": "Transport and Logistics", "description": "Understand logistics, transportation, and supply chain management."},
        {"title": "Office Administration", "description": "Develop the skills necessary for efficient office management."},
        {"title": "Corporate Management", "description": "Learn how to manage and lead corporations effectively."},
        {"title": "Cost Management Accounting", "description": "Understand cost accounting principles and cost management."},
        {"title": "Supervisory Management", "description": "Develop supervisory skills to manage teams effectively."},
        {"title": "Hospitality Management", "description": "Learn the principles of managing hospitality businesses."},
        {"title": "Travel and Tourism", "description": "Understand the travel and tourism industry and its management."},
        {"title": "Computer Programming", "description": "Learn to code in various programming languages."},
        {"title": "Basic Computing", "description": "Get introduced to the basics of computing and IT."},
        {"title": "Graphic Designing", "description": "Master the tools and techniques of graphic design."},
        {"title": "Business Administration", "description": "Learn the principles of managing and running businesses."},
        {"title": "Journalism", "description": "Develop skills in reporting, writing, and media production."},
        {"title": "Web Development", "description": "Learn to build and maintain websites."}
    ]
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
