
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    from app.api.routes import api
    app.register_blueprint(api, url_prefix='/api')
    return app
