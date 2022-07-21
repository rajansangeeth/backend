from flask import Flask
from flask_restful import Api
from database.db_connection import create_database
from routes import initialize_routes
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
cors = CORS(app, support_credentials=True)

app.config['CORS_HEADERS'] = 'application/json'
app.config['JWT_SECRET_KEY'] = "sangeeth"
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
initialize_routes(api)
create_database()
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)