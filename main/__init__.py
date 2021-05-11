from flask import Flask


def create_app():
    app = Flask("Qileb")
    app.config.from_object("config.Config")
    return app