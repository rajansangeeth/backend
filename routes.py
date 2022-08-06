from backup.resources.persons import PracticeQuery, Reduce
from resources.login import LoginApi
from resources.signup import SignupApi
from resources.users import UsersApi
from resources.persons import PersonApi, PersonEyeColor, PersonsIn, PersonFetchAll, PersonDate, AggregatePersons, Getone, InsertData
from resources.upload import Upload


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/sign-up')
    api.add_resource(LoginApi, '/api/login')
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(PersonApi, '/api/person')
    api.add_resource(PersonEyeColor, '/api/person/eyecolor')
    api.add_resource(PersonsIn, '/api/person/in')
    api.add_resource(PersonFetchAll, '/api/person/fetch_all')
    api.add_resource(PersonDate, '/api/persons/date')
    api.add_resource(AggregatePersons, '/api/aggregate')
    api.add_resource(Getone, '/api/getone')
    api.add_resource(InsertData, '/api/insertone')
    api.add_resource(Upload, '/api/uploadfile')
    api.add_resource(PracticeQuery, '/api/practice/query')
    api.add_resource(Reduce, '/api/reduce_methods')
