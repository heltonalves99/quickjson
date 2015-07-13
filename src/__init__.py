# -*- coding: utf-8 -*-
from bottle import Bottle
from bottle import static_file

from controllers import generate_json


root_app = Bottle()

@root_app.route('/:path#(images|css|js|fonts)\/.+#')
def server_static(path):
    return static_file(path, root='../public/static')


root_app.mount('/generate', generate_json.app)
