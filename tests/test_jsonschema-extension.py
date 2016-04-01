import os
import unittest

import json

from flask import Flask
from flask_jsonschema import JsonSchemaExtension

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, '../example_schemas')
jsonschema = JsonSchemaExtension(app)


@app.route('/books', methods=['POST'])
def books():
    return 'success'

client = app.test_client()

class JsonSchemaTests(unittest.TestCase):
    def test_valid_json(self):
        r = client.post(
            '/books',
            content_type='application/json',
            data=json.dumps({
                'title': 'Infinite Jest',
                'author': 'David Foster Wallace'
            })
        )
        self.assertIn('success', r.data)

    def test_invalid_json(self):
        r = client.post(
            '/books',
            content_type='application/json',
            data=json.dumps({
                'title': 'Infinite Jest'
            })
        )
        self.assertIn('error', r.data)
