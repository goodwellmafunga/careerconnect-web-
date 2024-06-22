from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Student, Course, Staff, Note, QuestionPaper
from app.forms import CourseForm, StaffForm, NoteForm, QuestionPaperForm
from app import db

admin = Blueprint('admin', __name__)

@admin.route('/admin/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('main.index'))
    return render_template('admin/dashboard.html')

@admin.route('/admin/manage_students')
@login_required
def manage_students():
    if not current_user.is_admin:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('main.index'))
    students = Student.query.all()
    return render_template('admin/manage_students.html', students=students)

@admin.route('/admin/manage_courses', methods=['GET', 'POST'])
@login_required
def manage_courses():
    if not current_user.is_admin:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('main.index'))
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(title=form.title.data, description=form.description.data)
        db.session.add(course)
        db.session.commit()
        flash('Course created successfully', 'success')
        return redirect(url_for('admin.manage_courses'))
    courses = Course.query.all()
    return render_template('admin/manage_courses.html', form=form, courses=courses)

@admin.route('/admin/upload_materials', methods=['GET', 'POST'])
@login_required
def upload_materials():
    if not current_user.is_admin:
        flash('Unauthorized access', 'danger')
        return redirect(url_for('main.index'))
    note_form = NoteForm()
    qp_form = QuestionPaperForm()
    if note_form.validate_on_submit() and 'note_file' in request.files:
        note_file = request.files['note_file']
        note = Note(course_id=note_form.course_id.data, filename=note_file.filename, data=note_file.read())
        db.session.add(note)
        db.session.commit()
        flash('Note uploaded successfully', 'success')
    if qp_form.validate_on_submit() and 'qp_file' in request.files:
        qp_file = request.files['qp_file']
        qp = QuestionPaper(course_id=qp_form.course_id.data, filename=qp_file.filename, data=qp_file.read())
        db.session.add(qp)
        db.session.commit()
        flash('Question Paper uploaded successfully', 'success')
    return render_template('admin/upload_materials.html', note_form=note_form, qp_form=qp_form)
