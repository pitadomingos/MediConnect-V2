# Contains the database structure using SQLAlchemy
from sqlalchemy import column
from sqlalchemy.orm import backref
from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model:
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  role = db.Column(db.String(64)) # admin, doctor, nurse, user, etc.
  patients = db.relationship('Patient', backref='user', lazy='dynamic')

class Patient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=True)
  dob = db.Column(db.DateTime)
  gender = db.Column(db.String(64))
  address = db.Column(db.String(128))
  phone = db.Column(db.String(64))
  email = db.Column(db.String(120))
  allergies = db.Column(db.String(128))
  home_clinic = db.Column(db.String(64))
  next_of_keen - db.Column(db.String(64))
  keen_contact = db.Column(db.String(64))
  photo = db.Column(db.LargeBinary)
  history = db.column('DiagnosisHistory', backref=backref('patient', lazy='dynamic')

classe DiagnosisHistory(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
  date = db.Column(db.DateTime, default=datetime.utcnow)
  diagnosis = db.Column(db.Text)
  prescription = db.column(db.Text)
  clinic = db.Column(db.String(120))