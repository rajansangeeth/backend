from models.procedure import Procedure
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from flask import request
from models.user import Users

class CreateProcedure(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        active_user = Users.objects.get(email=user_id)
        data = request.get_json()
        steps = []
        return {'result': 'Procedure created successfully'}, 200