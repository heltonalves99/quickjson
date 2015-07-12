from bottle import Bottle

from controllers import generate_json


root_app = Bottle()

root_app.mount('/generate', generate_json.app)
