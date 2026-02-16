from flask import Flask
from epl.extension import db, migrate
from epl.core.routes import core_bp
from epl.clubs.routes import clubs_bp
from epl.players.routes import players_bp
# from epl.models import Club, Player

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///epl.db'
    app.secret_key = b'asjdlkdjlkasdjlkasjdlkjasdjasdlk'

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(clubs_bp, url_prefix='/clubs')
    app.register_blueprint(players_bp, url_prefix='/players')


    return app