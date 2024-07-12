from flask import Flask, render_template,jsonify, request, redirect, url_prefix  
from flask_jwt_extapp.ended import JWTManager
from flask_migrate import Migrate
from models import db
from config import Config
from routes.auth import auth_bp
from routes.doctors import doctors_bp
from routes.appointments import appointments_bp
from routes.telehealth import telehealth_bp
import requests

app = Flask(__name__, static_folder='web-static', template_folder='templates')
app.config.from_object(Config)

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(doctors_bp, url_prefix='/api')
app.register_blueprint(appointments_bp, url_prefix='/api')
app.register_blueprint(telehealth_bp, url_prefix='/api')

@app.route('/')
def home():
    print('Welcome to AccessHealth!')
    print('Revolutionizing Patient-Doctor Interactions')
    return render_template('index.html')

@app.route('/<template>')
def serve_template(template):
    try:
        return render_template(f'{template}.html')
    except Template Not Found:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500
def get_doctors():
    url = 'https://accesshealth.onrender.com/api/doctors'
    try:
        response = requests.get(url)
        response.raise_for_status()
        doctors = response.json()
        return jsonify(doctors)
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)}), 500
    

    
if __name__ == '__main__':
    app.run(debug=True)

