from flask import Flask

# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_pybo():  # put application's code here
#     return 'Hello, Pybo!'
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, structure_views, user_views, structur_tiltmeter_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(structure_views.bp)
    app.register_blueprint(structur_tiltmeter_views.bp)
    app.register_blueprint(user_views.bp)

    return app