# users-service/project/__init__.py
import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_swagger import swagger

# instantiate the db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()



def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.debug = True
    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    # register blueprints
    from finager_rest.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    from finager_rest.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)



    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
