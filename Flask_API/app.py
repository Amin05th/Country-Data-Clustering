from flask import Flask, Blueprint, render_template, url_for
import pandas as pd
import numpy as np
from Flask_API import settings
from Flask_API.api.myapi import api
from Flask_API.api.endpoints.all_countries import namespace as all_countries_namespace
from Flask_API.api.endpoints.single_country import namespace as single_country_namespace
from Flask_API.api.database.db import db, get_all_countries, get_all_countries_arr
import flagpy as fp
import io
import base64

app = Flask(__name__)


def fetch_country_images():
    all_countries = get_all_countries_arr()
    print(all_countries)
    background_uri_array = {}
    for country in all_countries:
        try:
            image = fp.get_flag_img(country)
            with io.BytesIO() as buffer:
                image.save(buffer, "JPEG")
                data = base64.b64encode(buffer.getvalue()).decode("ascii")
                background_uri = f"data:image/jpeg;base64,{data}"
                background_uri_array[country] = background_uri
        except Exception:
            background_uri_array[country] = ""
    return background_uri_array


@app.route("/")
def index():
    all_countries = get_all_countries()
    background_dict = fetch_country_images()
    return render_template("index.html", all_countries=all_countries, background_dict=background_dict)


def configure_app(app):
    app.config["RESTPLUS_SWAGGER_EXPANSION"] = settings.RESTPLUS_SWAGGER_EXPANSION
    app.config["RESTPLUS_VAL"] = settings.RESTPLUS_VAL
    app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODS"] = settings.SQLALCHEMY_TRACK_MODS


def init(app):
    configure_app(app)
    blueprint = Blueprint("country_clustering_api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(all_countries_namespace)
    api.add_namespace(single_country_namespace)
    db.init_app(app)
    app.register_blueprint(blueprint)


def main():
    init(app)
    app.run(host=settings.FLASK_HOST,
            debug=settings.FLASK_DEBUG_MODE,
            port=settings.FLASK_PORT,
            threaded=settings.FLASK_THREADED)


if __name__ == '__main__':
    main()
