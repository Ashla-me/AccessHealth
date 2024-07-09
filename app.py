from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db
from config import Config
from routes.auth import auth_bp
from routes.doctors import doctors_bp
from routes.appointments import appointments_bp
from routes.telehealth import telehealth_bp

app = Flask(__name__, static_folder='web-static', template_folder='template')
app.config.from_object(Config)

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(doctors_bp, url_prefix='/api')
app.register_blueprint(appointments_bp, url_prefix='/api')
app.register_blueprint(telehealth_bp, url_prefix='/api')

@app.route('/<template>')
def serve_template(template):
    try:
        return render_template(f'{template}.html')
    except TemplateNotFound:
        return "Template not found", 404

if __name__ == '__main__':
    app.run(debug=True)

