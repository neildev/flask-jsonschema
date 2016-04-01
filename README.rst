Flask-JsonSchema
================

JSON request validation for Flask applications.

Place schemas in the specified ``JSONSCHEMA_DIR``. 

.. code-block:: python

    import os

    from flask import Flask, request
    from flask_jsonschema import JsonSchema, ValidationError

    app = Flask(__name__)
    app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'schemas')

    jsonschema = JsonSchema(app)

    @app.route('/books', methods=['POST'])
    def create_book():
        # create the book
        return 'success'

The schema for the example above should be named ``books.json`` and should
reside in the configured folder. It should look like so:

.. code-block:: json

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "http://jsonschema.net",
      "type": "object",
      "properties": {
        "title": {
          "id": "http://jsonschema.net/title",
          "type": "string"
        },
        "author": {
          "id": "http://jsonschema.net/author",
          "type": "string"
        }
      },
      "required": [
        "title",
        "author"
      ]
    }

With this example configuration, someone who POST's json not conforming to the 
book schema would recieve a response like the following:

.. code-block:: json

{"error_message": "'title' is a required property\n\nFailed validating 'required' in schema:\n    {'$schema': 'http://json-schema.org/draft-04/schema#',\n     'id': 'http://jsonschema.net',\n     'properties': {'author': {'id': 'http://jsonschema.net/author',\n                               'type': 'string'},\n                    'title': {'id': 'http://jsonschema.net/title',\n                              'type': 'string'}},\n     'required': ['title', 'author'],\n     'type': 'object'}\n\nOn instance:\n    {}", "error": "request_validation_failed"}



Resources
---------

- `Issue Tracker <http://github.com/mattupstate/flask-jsonschema/issues>`_
- `Code <http://github.com/mattupstate/flask-jsonschema/>`_