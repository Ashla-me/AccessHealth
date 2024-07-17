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
