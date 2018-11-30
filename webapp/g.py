import flask
import psycopg2.extras
from werkzeug.local import LocalProxy


def get_db():
    # pylint: disable=redefined-outer-name
    db = getattr(flask.g, '_database', None)
    if db is None:
        db = flask.g._database = psycopg2.connect(
            'dbname=webapp',
            cursor_factory=psycopg2.extras.DictCursor,
        )
    return db


db = LocalProxy(get_db)
