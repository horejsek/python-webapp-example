import flask

from .config import register_config


app = flask.Flask(__name__)

register_config(app)


@app.route('/')
def homepage() -> str:
    return flask.render_template('index.html')
