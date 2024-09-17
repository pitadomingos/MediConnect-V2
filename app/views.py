# THis file manages the functionality of the application

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.Models import Patient, DiagnosisHistory
from app.forms import SearchForm
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
  form = SearchForm()
  if form.validate_on_submit():
    patient = Patient.query.filter_by(name=form.name.data).first()
    if patient is None:
      flash('Patient not found')
      return redirect(url_for('main.dashboard'))
    else:
      return redirect(url_for('main.patient', patient_id=patient.id))
  return render_template('main/dashboard.html', form=form)

@main_bp.route('/patient/<int:patient_id>/history')
@login_required
def patient_history(patient_id):
  patient = Patient.query.get_or_404(patient_id)
  history = patient.history.order_by(DiagnosisHistory.date.desc()).limit(20).all()
  return render_template('main/patient_history.html', patient=patient, history=history)