from flask import Blueprint, request, jsonify
from models import db, Appointment, Consultation
from config import Config
from utils.decorators import role_required

telehealth_bp = Blueprint('telehealth_bp', __name__)

@telehealth_bp.route('/telehealth/start', methods=['POST'])
@role_required('doctor')
def start_telehealth_session():
    data = request.get_json()
    appointment = Appointment.query.filter_by(appointment_id=data['appointment_id']).first()
    if appointment:
        room = client.video.rooms.create(unique_name=f"Appointment_{data['appointment_id']}")
        consultation = Consultation(
            consultation_id=f"consult_{data['appointment_id']}",
            appointment_id=data['appointment_id'],
            session_link=room.sid
        )
        db.session.add(consultation)
        db.session.commit()
        return jsonify(session_link=room.sid), 201
    return jsonify(message="Appointment not found"), 404

@telehealth_bp.route('/telehealth/status', methods=['GET'])
@role_required('doctor')
def get_telehealth_status():
    session_id = request.args.get('session_id')
    session = Consultation.query.filter_by(consultation_id=session_id).first()
    if session:
        return jsonify({'consultation_id': session.consultation_id, 'appointment_id': session.appointment_id, 'session_link': session.session_link, 'notes': session.notes, 'recording': session.recording}), 200
    return jsonify(message="Session not found"), 404

