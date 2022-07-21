from models.login import LoginActivity
from models.signup import Signup
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from datetime import timedelta


class LoginApi(Resource):
    # def post(self):
    #     data = request.get_json()
    #     if Signup.objects(email=data['email']).count() == 0:
    #         return {'message': 'Email not exists'}, 400
    #
    #     signup = Signup.objects.get(email=data['email'])
    #     authorized = signup.check_pwd(data['password'])
    #     print(authorized)
    #
    #     if not authorized:
    #         return {'message': 'Invalid credentials'}, 400
    #
    #     expires = timedelta(hours=2) if signup.category == 'Non-Prime' else timedelta(hours=3)
    #     token = create_access_token(identity=signup.email, expires_delta=expires)
    #     print(token)
    #     login = LoginActivity()
    #     login.email = data['email']
    #     login.save()
    #
    #     return {'result': token}, 200

    def post(self):
        data = request.get_json()
        if Signup.objects(email=data['email']).count() == 0:
            return {'message': 'User not exists'}, 400

        user = Signup.objects.get(email=data['email'])
        authorized = user.check_pwd(data['password'])

        if authorized:
            expires = timedelta(minutes=1) if user.category == "Non-prime" else timedelta(minutes=2)
            access_token = create_access_token(identity=data['email'], expires_delta=expires)
            activity = LoginActivity()
            activity.email = data['email']
            activity.save()

            return {'result': access_token}, 200
