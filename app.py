from flask import Flask, request, redirect, render_template
from admin.Admin import start_views

from config import app_config, app_active

from flask_sqlalchemy import SQLAlchemy

# controllers
from controller.User import UserController

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # database
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(config.APP)
    
    # start admin
    app.config['FLASK_ADMIN_SWATCH'] = 'simplex'
    start_views(app, db);
    
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello World'

    @app.route('/login')
    def login():
        return 'tela de login'

    @app.route('/login', methods = ['POST'])
    def login_post():
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        login_response = user.login(email, password)

        if login_response:
            return redirect('/admin')
        else:
            return render_template(
                'login.html',
                data = {
                    'status': 401,
                    'message': 'Dados de usuário incorretos',
                    'type': None
                }
            )
    
    @app.route('/recovery-passowrd')
    def recovery_password():
        return 'recovery password'

    @app.route('/recovery-password', methods = ['POST'])
    def recovery_password_post():
        user = UserController()

        email = request.form['email']
        recovery_response = user.recovery(email)

        return render_template(
            'recovery.html',
            data = {
                'status': 200,
                'message': 'Se o e-mail informado estiver correto o e-mail de recuperção foi enviado. Confira o SPAM'
            }
        )


    return app