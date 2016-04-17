# -*- coding: utf-8 -*-
"""
    flask_jsonschema
    ~~~~~~~~~~~~~~~~

    flask_jsonschema
"""

import json
import os

from flask import request
import jsonschema


class JsonSchemas(object):
    def __init__(self, schemas):
        self.schemas = schemas

    def get_schema(self, path):
        return self.schemas[path]

def load_schemas_from_dir(schema_dir):
    schemas = {}
    for fn in os.listdir(schema_dir):
        key = fn.split('.')[0]
        fn = os.path.join(schema_dir, fn)
        if os.path.isdir(fn) or not fn.endswith('.json'):
            continue
        with open(fn) as f:
            schemas["/"+key] = json.load(f)
    return schemas

class JsonSchemaExtension(object):
    def __init__(self, app=None, schemas=None):
        if schemas is None:
            default_dir = os.path.join(app.root_path, 'jsonschema')
            schema_dir = app.config.get('JSONSCHEMA_DIR', default_dir)
            schemas = load_schemas_from_dir(schema_dir)
        self.jsonschemas = JsonSchemas(schemas)

        if app is not None:
            self.init_app(app)

    def init_app(self, app, schemas=None):
        if app.before_request_funcs is None:
            app.before_request_funcs = {}
        app.before_request_funcs.setdefault(None, [])
        app.before_request_funcs[None].append(self.validate_current_request)
        app.register_error_handler(jsonschema.ValidationError, self.handle_json_validation_error)

    def validate_current_request(self):
        if request.method != "POST" and request.method != "PUT":
            return
        # schemas should match the class of object not the instance, therefore we take the following
        # path "/WorldObject/Home" or "/WorldObjecs" should match the "worldobjects" schema
        print '/'.join(request.path.lower().split('/')[:-1:])
        print '/'.join(request.path.lower().split('/')[:-1:])+'s'
        try: 
            schema = self.jsonschemas.get_schema('/'.join(request.path.lower().split('/')[:-1:]))
        except KeyError:
            try:
                schema = self.jsonschemas.get_schema('/'.join(request.path.lower().split('/')[:-1:])+'s')
            except KeyError:
                raise KeyError
        jsonschema.validate(request.json, schema)

    def handle_json_validation_error(self, json_validation_error):
        return json.dumps({"error":"request_validation_failed", "error_message":str(json_validation_error)}), 422
        
