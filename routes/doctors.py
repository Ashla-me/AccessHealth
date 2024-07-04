from flask import Blueprint, request, jsonify
from models import db, Doctor
from utils.decorators import role_required

doctors_bp = Blueprint('doctors_bp', __name__)

@doctors_bp.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    doctors_list = [{'doctor_id': doc.doctor_id, 'specialty': doc.specialty, 'availability': doc.availability, 'rating': doc.rating} for doc in doctors]
    return jsonify(doctors_list), 200

@doctors_bp.route('/doctors/<doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.filter_by(doctor_id=doctor_id).first()
    if doctor:
        return jsonify({'doctor_id': doctor.doctor_id, 'specialty': doctor.specialty, 'availability': doctor.availability, 'rating': doctor.rating}), 200
    return jsonify(message="Doctor not found"), 404

@doctors_bp.route('/doctors', methods=['POST'])
@role_required('doctor')
def add_doctor():
    data = request.get_json()
    new_doctor = Doctor(
        doctor_id=data['doctor_id'],
        specialty=data['specialty'],
        availability=data['availability'],
        rating=data['rating']
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify(message="Doctor profile added successfully"), 201

