# -*- coding: utf-8 -*-
import os
from bottle import Bottle, TEMPLATE_PATH
from bottle import static_file
from controllers import generate_json

TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

root_app = Bottle()

@root_app.route('/:path#(images|css|js|fonts)\/.+#')
def server_static(path):
    return static_file(path, root='../public/static')


root_app.mount('/generate', generate_json.app)
