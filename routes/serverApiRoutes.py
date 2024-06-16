from flask_restful import Api

from Api.test import TestUpload
from routes.fontRoutes import app_bp

SERVER_API = "/server_api"


def register_route(app):
    app.register_blueprint(app_bp)

    api = Api(app)

    api.add_resource(TestUpload, f'{SERVER_API}/upload')
