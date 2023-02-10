from flask import flask
def create_app (config_file='settings.py'):
    app = flask(__name__, static_url_path="/tmp", static_folder="tmp")
    app.config.from_pyfile(config_file)

    app.register_blueprint(generator)
    return app 