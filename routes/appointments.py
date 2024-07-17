from flask import Blueprint, request, jsonify
from models import db
from flask_jwt_extended import get_jwt_identity
from models import Appointment
from utils.decorators import role_required

appointments_bp = Blueprint('appointments_bp', __name__)

@appointments_bp.route('/appointments', methods=['POST'])
@role_required('patient')
def book_appointment():
    data = request.get_json()
    current_user = get_jwt_identity()
    appointment = Appointment(
        appointment_id=data['appointment_id'],
        doctor_id=data['doctor_id'],
        patient_id=current_user['email'],
        date=data['date'],
        time=data['time']
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify(message="Appointment booked successfully"), 201

@appointments_bp.route('/appointments/<appointment_id>', methods=['GET'])
@role_required('patient')
def get_appointment(appointment_id):
    appointment = Appointment.query.filter_by(appointment_id=appointment_id).first()
    if appointment:
        return jsonify({'appointment_id': appointment.appointment_id, 'doctor_id': appointment.doctor_id, 'patient_id': appointment.patient_id, 'date': appointment.date, 'time': appointment.time, 'status': appointment.status}), 200
    return jsonify(message="Appointment not found"), 404

