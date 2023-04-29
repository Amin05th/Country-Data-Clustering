from flask_restx import Api

api = Api(version="0.1", title="country_clustering", description="This is a open source Api used it to your needs")


@api.errorhandler(Exception)
def error(err):
    return "unexpected error occurred", err


