from flask import jsonify
from flask_restx import Namespace, Resource
from Flask_API.api.myapi import api
from Flask_API.api.database.db import get_single_country

namespace = Namespace(api=api, name="")


@namespace.route("/<int:country_id>")
class Get_all_countries(Resource):
    def get(self, country_id):
        return jsonify(get_single_country(country_id))
