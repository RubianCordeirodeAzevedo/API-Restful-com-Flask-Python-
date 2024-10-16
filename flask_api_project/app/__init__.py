from flask import Flask
from app.routes import api

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(api, url_prefix='/api')

from app import models
