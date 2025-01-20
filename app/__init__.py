from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    # Create a test route
    @app.route('/test', methods=['GET'])
    def test():
      return make_response(jsonify({'message': 'test route'}), 200)

    return app

from app import models
