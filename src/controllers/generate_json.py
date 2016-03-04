# -*- coding: utf-8 -*-
import os
from bottle import Bottle, request, response
from bottle import jinja2_template as template
from bottle import TEMPLATE_PATH
from faker import Faker
import urlparse
import requests
import pickle
import uuid
import redis
import json

from __init__ import enable_cors


TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

app = Bottle()


def mount_json(object_base):
    fake = Faker()
    fake.__dict__['list_email'] = ''
    fake.__dict__['image'] = ''
    fake.__dict__['list_image'] = ''
    fake.__dict__['from'] = ''
    obj = {}
    for key, value in object_base.items():
        if isinstance(value, dict):
            obj[key] = mount_json(value)
            continue
        if isinstance(value, list):
            if value[0] in dir(fake):
                try:
                    if value[0] == 'list_email':
                        obj[key] = [fake.email() for n in range(value[1])]
                        continue
                    if value[0] == 'image':
                        obj[key] = 'http://placehold.it/{}'.format(value[1])
                        continue
                    if value[0] == 'list_image':
                        obj[key] = ['http://placehold.it/{}'.format(value[1]) for n in range(value[2])]
                        continue
                    if value[0] == 'from':
                        url_from = urlparse.urlsplit(value[1])
                        if url_from.netloc == 'quickjson.com':
                            uid_from = url_from.path.split('/')[2]
                            try:
                                count_from = url_from.query.split('=')[1]
                            except IndexError:
                                count_from = ''

                            obj[key] = generate_json(uid_from, count_from)
                            continue
                        obj[key] = requests.get(value[1]).json()
                        continue

                    func = getattr(fake, value[0])
                    obj[key] = func(value[1])
                except IndexError:
                    func = getattr(fake, value[0])
                    obj[key] = func()
                continue

            obj = {}
            break

    return obj


def generate_json(uid, count):
    result = {}
    r_server = redis.Redis()
    obj_json = r_server.get(uid)

    if obj_json:
        obj_json = pickle.loads(obj_json)
        try:
            result = [mount_json(obj_json) for n in range(int(count))]
        except ValueError:
            result = mount_json(obj_json)
        return result

    result['error'] = 'URL invalid or expired!'
    return result


@app.route('/', method='POST')
def index():
    result = {}
    valid_time = int(request.forms.get('valid_time'))
    json_base = request.forms.get('json_base')

    try:
        object_base = json.loads(json_base)
        if not mount_json(object_base):
            result['error'] = 'Error converting the base JSON.'
            return template('index.html', {'response': result})

        key_object = uuid.uuid4().hex[:12]
        # Connection with Redis
        r_server = redis.Redis('localhost')
        redis_key = key_object
        r_server.set(redis_key, pickle.dumps(object_base))
        r_server.expire(redis_key, valid_time)

        result['key_object'] = key_object
    except ValueError:
        result['error'] = 'Error converting the base JSON.'

    return template('index.html', {'response': result})


@app.route('/<uid>', method='GET')
@enable_cors
def get_json(uid):
    count = request.query.get('count', '')
    response.content_type = 'application/json'
    return json.dumps(generate_json(uid, count))
