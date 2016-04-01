"""
Flask-JsonSchema
----------

A Flask extension for validating JSON requets with jsonschema

"""
from setuptools import setup, find_packages


setup(
    name='Flask-JsonSchema',
    version='0.2.0',
    url='https://github.com/hurricanelabs/flask-jsonschema',
    license='MIT',
    author='Hurricane Labs',
    author_email='dev@hurricanelabs.com',
    description='Flask extension for validating JSON requets',
    long_description=__doc__,
    package_dir = {"":"src"},
    packages = find_packages("src"),
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=0.9', 'jsonschema>=1.1.0'],
    tests_require=['nose'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
