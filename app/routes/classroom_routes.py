from flask import Blueprint, render_template
from flask_login import login_required

classroom = Blueprint('classroom', __name__)

@classroom.route('/classrooms')
@login_required
def classrooms():
    return render_template('classrooms.html')
