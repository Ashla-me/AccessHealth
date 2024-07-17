from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import Doctor, db
from config import Config
from flask_cors import CORS
import requests

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='template')
    app.config.from_object(Config)

    # initializes extensions
    jwt = JWTManager(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)
    
    # imports and registers Blueprints
    from routes.auth import auth_bp
    from routes.doctors import doctors_bp
    from routes.appointments import appointments_bp
    from routes.telehealth import telehealth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(doctors_bp, url_prefix='/api/doctors')
    app.register_blueprint(appointments_bp, url_prefix='/api/appointments')
    app.register_blueprint(telehealth_bp, url_prefix='/api/telehealth')

    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        print('Welcome to AccessHealth!')
        return render_template('index.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/patients', methods=['GET'])
    def get_patients():
        patients = patients.query.all()
        patient_list = [{'id': patient.id, 'name': patient.name, 'age': patient.age, 'medical_history': patient.medical_history} for patient in patients]
        return jsonify(patient_list)
    
    @app.route('/doctors', methods=['GET'])
    def get_doctors():
        try:
            doctors = Doctor.query.all()
            doctors_list = [doctor.to_dict() for doctor in doctors]
            return jsonify(doctors_list) 
        except Exception as err:
            return jsonify({"error": str(err)}), 500
    
    @app.route('/appointments')
    def appointment():
        return render_template('appointments.html')

    @app.route('/doctors_view')
    def doctors_view():
        return render_template('doctors.html')

    return app

if __name__ == '__main__':

    app = create_app()
    app.run(debug=True)
