from models.signup import Signup
from flask import request
from flask_restful import Resource


class SignupApi(Resource):
    def post(self):
        data = request.get_json()

        if Signup.objects(email=data['email']).count() > 0:
            return {'message': 'Email already exists'}, 400

        signup = Signup(**data)
        signup.first_name = signup.first_name.strip()
        signup.last_name = signup.last_name.strip()
        signup.email = signup.email.strip()
        signup.hash_pwd()
        signup.save()

        return {'result': 'User registered successfully'}, 200
