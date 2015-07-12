# -*- coding: utf-8 -*-
from bottle import Bottle, request
from bottle import jinja2_template as template
from faker import Faker
import pickle
import uuid
import redis
import json

app = Bottle()

def mount_json(object_base):
    fake = Faker()
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

                    func = getattr(fake, value[0])
                    obj[key] = func(value[1])
                except IndexError:
                    func = getattr(fake, value[0])
                    obj[key] = func()
                continue

            obj = {}
            break

    return obj


@app.route('/', method='POST')
def index():
    response = {}
    valid_time = int(request.forms.get('valid_time'))
    json_base = request.forms.get('json_base')

    try:
        object_base = json.loads(json_base)
        if not mount_json(object_base):
            response['error'] = 'Error trying convert the base JSON.'
            return template('index.html', {'response': response})

        key_object = uuid.uuid4().hex[:12]
        # Connection with Redis
        r_server = redis.Redis('localhost')
        redis_key = key_object
        r_server.set(redis_key, pickle.dumps(object_base))
        r_server.expire(redis_key, valid_time)

        response['key_object'] = key_object
    except ValueError:
        response['error'] = 'Error trying convert the base JSON.'

    return template('index.html', {'response': response})


@app.route('/<uid>', method='GET')
def generate_json(uid):
    response = {}
    r_server = redis.Redis()
    obj_json = r_server.get(uid)

    if obj_json:
        obj_json = pickle.loads(obj_json)
        try:
            count = int(request.query.get('count', ''))
            response = [mount_json(obj_json) for n in range(count)]
        except ValueError:
            response = mount_json(obj_json)

        return json.dumps(response)

    response['error'] = 'URL invalid or expired!'
    return json.dumps(response)
