"""
Module of config files for all environemnts.

Every environment is one sub-module and is imported to the Flask
config by ENV variable called WEBAPP_ENV. If you set up that
variable to ``dev``, module ``webapp.config.dev`` is used.
"""

import os


DEFAULT_ENV = 'prod'


def register_config(app):
    app.config.from_object('webapp.config.{}'.format(get_env()))


def get_env():
    return os.getenv('WEBAPP_ENV', DEFAULT_ENV)
