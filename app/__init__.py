from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        from .routes import main_routes, auth_routes, admin_routes, classroom_routes
        app.register_blueprint(main_routes.main)
        app.register_blueprint(auth_routes.auth)
        app.register_blueprint(admin_routes.admin)
        app.register_blueprint(classroom_routes.classroom)

        db.create_all()  # Ensure tables are created

        return app
