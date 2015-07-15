# -*- coding: utf-8 -*-
import os
from bottle import run
from bottle import jinja2_template as template

from __init__ import root_app


@root_app.route('/', method='GET')
def index():
    return template('index.html', {})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    run(root_app, host='0.0.0.0', port=port, debug=True)
