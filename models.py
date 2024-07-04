from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.String(50), unique=True, nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float, nullable=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.String(50), unique=True, nullable=False)
    doctor_id = db.Column(db.String(50), db.ForeignKey('doctor.doctor_id'), nullable=False)
    patient_id = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consultation_id = db.Column(db.String(50), unique=True, nullable=False)
    appointment_id = db.Column(db.String(50), db.ForeignKey('appointment.appointment_id'), nullable=False)
    session_link = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    recording = db.Column(db.String(200), nullable=True)

