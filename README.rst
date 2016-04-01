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
      "create": {
        "type": "object",
        "properties": {
          "title": {},
          "author": {}
        },
        "required": ["title", "author"]
      },
      "update": {
        "type": "object",
        "properties": {
          "title": {},
          "author": {}
        }
      }
    }

Notice the top level action names. Flask-JsonSchema supports one "path" level so
that you can organize related schemas in one file. If you do not wish to use this
feature you can simply use one schema per file and remove the second parameter
to the ``@jsonschema.validate`` call.

With this example configuration, someone who POST's json not conforming to the 
book schema would recieve a response like the following:

Resources
---------

- `Issue Tracker <http://github.com/mattupstate/flask-jsonschema/issues>`_
- `Code <http://github.com/mattupstate/flask-jsonschema/>`_