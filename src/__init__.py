# -*- coding: utf-8 -*-
import bottle
from bottle import Bottle
from bottle import static_file
from settings import TEMPLATE_PATH
from controllers import generate_json

bottle.TEMPLATE_PATH.insert(0, TEMPLATE_PATH)

root_app = Bottle()

@root_app.route('/:path#(images|css|js|fonts)\/.+#')
def server_static(path):
    return static_file(path, root='../public/static')


root_app.mount('/generate', generate_json.app)
