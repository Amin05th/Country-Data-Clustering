from flask import jsonify
from flask_restx import Namespace, Resource
from Flask_API.api.myapi import api
from Flask_API.api.database.db import get_all_countries

namespace = Namespace(api=api, name="")


@namespace.route("/all")
class Get_all_countries(Resource):
    def get(self):
        return jsonify(get_all_countries())
