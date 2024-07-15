from flask import Flask, render_template,jsonify, request
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db
from config import Config
from routes.auth import auth_bp
from routes.doctors import doctors_bp
from routes.appointments import appointments_bp
from routes.telehealth import telehealth_bp
from flask_cors import CORS
import requests
import logging

app = Flask(__name__, static_folder='web-static', template_folder='template')

app.config['SECRET_KEY'] = 'ae3ecc52f525b916cb484cd7cc74c077c7ab04f0651206d6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ASHla1212!@localhost/bite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '861af9062c612f4352007ea17eb8c1545857418b3007e36b024daec9bf7861c5'
logging.basicConfig(level=logging.DEBUG)

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(doctors_bp, url_prefix='/api')
app.register_blueprint(appointments_bp, url_prefix='/api')
app.register_blueprint(telehealth_bp, url_prefix='/api')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    print('Welcome to AccessHealth!')
    app.logger.debug('Rendering home page')
    return render_template('index.html')

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    patient_list = [{'id': patient.id, 'name': patient.name, 'age': patient.age, 'medical_history': patient.medical_history} for patient in patients]
    return jsonify(patient_list)

#@app.route('/<template>')
def serve_template(template):
    try:
        return render_template(f'{template}.html')
    except TemplateNotFound:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500
    
def get_doctors():
    url = 'https://localhost:5000/api/doctors'
    try:
        response = requests.get(url)
        response.raise_for_status()
        doctors = response.json()
        return jsonify(doctors)
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)}), 500#
    
if __name__ == '__main__':
    app.run(debug=True)

