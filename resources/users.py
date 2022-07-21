from models.user import Users
from flask_restful import request, Resource
from flask import request, json


class UsersApi(Resource):
    def get(self):
        users = Users.objects()
        skip = 10
        args = request.args.to_dict()
        sort_by = "department"
        users_count = users.skip(10).limit(20).count()
        # users_count = users.skip(skip).limit(take).order_by(sort_by).to_json()
        print(users_count)
        print(json.loads(users_count))
        return {'result': users_count}

