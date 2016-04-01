# -*- coding: utf-8 -*-
"""
    flask_jsonschema
    ~~~~~~~~~~~~~~~~

    flask_jsonschema
"""

import json
import os

from flask import current_app, request
import jsonschema


class JsonSchema(object):
    def __init__(self, schemas):
        self._schemas = schemas

    def get_schema(self, path):
        rv = self._schemas[path[0]]
        for p in path[1:]:
            rv = rv[p]
        return rv

def load_schemas_from_dir(schema_dir):
    schemas = {}
    for fn in os.listdir(schema_dir):
        key = fn.split('.')[0]
        fn = os.path.join(schema_dir, fn)
        if os.path.isdir(fn) or not fn.endswith('.json'):
            continue
        with open(fn) as f:
            schemas[key] = json.load(f)
    return schemas

class JsonSchemaExtension(object):
    def __init__(self, app=None, schemas=None):
        if schemas is None:
            default_dir = os.path.join(app.root_path, 'jsonschema')
            schema_dir = app.config.get('JSONSCHEMA_DIR', default_dir)
            schemas = load_schemas_from_dir(schema_dir)
        self.jsonschema = JsonSchema(schemas)

        if app is not None:
            self.init_app(app)

    def init_app(self, app, schemas=None):
        if app.before_request_funcs is None:
            apps.before_request_funcs = {}
        app.before_request_funcs.setdefault(None, [])
        app.before_request_funcs[None].append(self.validate_current_request)

    def validate_current_request(self):
        schema = self._jsonschema.get_schema(path)
        try:
            jsonschema.validate(request.json, schema)
        except jsonschema.ValidationError:
            raise
