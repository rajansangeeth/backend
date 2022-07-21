from models.persons import Persons
from flask_restful import Resource
from flask import request
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from templates.text import mail_data

class PersonApi(Resource):
    @jwt_required()
    def get(self):
        args = request.args.to_dict()
        print(args)
        sort_by=''
        if 'order_by' in args:
            sort_by = args['order_by']
            del args['order_by']
        query2 = ""
        if "isActive__icontains" in args:
            if args['isActive__icontains'] == 'false':
                query2 = {
                    "$and": [{
                        "isActive": False
                    }]
                }
            elif args['isActive__icontains'] == 'true':
                query2 = {
                    "$and": [{
                        "isActive": True
                    }]
                }
            del args['isActive__icontains']
        take = 5
        names = []
        query = {
            "$and": [{
                "age" : 20
            }]
        }

        query1 = {
            "$or": [{
                "eyeColor": "blue"
            }]
        }

        # args = {"isActive__icontains": True}
        # args = {"isActive__icontains": False}

        pipeline = query and query1
        # persons = Persons.objects().limit(take).order_by("name")
        # persons = Persons.objects().filter(name__icontains = "ra").limit(take).order_by("age")
        # persons = Persons.objects().filter(name__icontains = "ra").limit(take).order_by("-age")
        # persons = Persons.objects(__raw__ = pipeline)
        # persons = Persons.objects()
        persons = Persons.objects(**args).limit(take).filter(__raw__=query2).order_by(sort_by)
        print(persons.count())
        for each in persons:
            names.append(each.name)

        return {'result': names}


class PersonEyeColor(Resource):
    @jwt_required()
    def get(self):
        eyecolor=[]
        persons = Persons.objects()
        for each in persons:
            eyecolor.append(each.eyeColor)
        return {'result': eyecolor}


class PersonsIn(Resource):
    @jwt_required()
    def get(self):
        person = Persons.objects(eyeColor__in=['blue','green'])
        result = []
        for each in person:
            result.append(each.eyeColor)

        args = [20,21]
        result1 = []
        samp = Persons.objects().filter(age__in=args)
        for each in samp:
            result1.append(each.age)

        return {'result': result, 'result1': result1}

class PersonFetchAll(Resource):
    # @jwt_required()
    def get(self):
        # person = Persons.objects(name__startswith='Au').update(__raw__ = {'$set' : {"is_deleted": False}})
        # person_date = json.loads(person.to_json())
        # total_count = person.count()

        # persons = Persons.objects(age__lte=30)
        # total_age = persons.sum('age')
        # return { 'total_count': total_count, 'result': person_date }

        # person_data = Persons.objects(age__ne=30)
        # person_data = Persons.objects(age__nin=[30, 25])
        # person_data = Persons.objects(age__lt=29, age__gt=30)
        # person = person_data.sum('age')

        # person_data = Persons.objects()
        # total_age = person_data.sum('age')
        # person = person_data.average('age')
        # return { 'results': person, 'total_age': total_age }

        # persons = Persons.objects.aggregate(pipeline)

        # person = json.loads(Persons.objects(age=29).exclude('name', 'age').to_json())
        # person = json.loads(Persons.objects(age=29).only('name', 'age').to_json())


        # query = [{
        #     "$project" : {'name':1, 'age': 1, 'company.location.country': 1}
        # }]
        # person = Persons.objects(age__mod=(2,1)).aggregate(pipeline=query)
        # persons = []
        # for each in person:
        #     persons.append(each)

        # persons = json.loads(Persons.objects[:10].to_json())
        persons = json.loads(Persons.objects().to_json())

        return {'results': persons}


class PersonDate(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        print(identity)
        persons = Persons.objects().to_json()
        date = []
        for each in persons:
            # print(each.registered)
            # date.append(each.registered)
            date.append((each['registered']))
            # date.append(datetime.strftime(each.registered["$date"]))

        return {'result': date}, 200


class AggregatePersons(Resource):
    @jwt_required()
    def get(self):
        query = [
            {"$group": {"_id": {"company":"$company.location.country", "age": "$age", "gender": "$gender"}}},
            {"$match": {"_id.gender": "female"}},
            {"$count": "total"}
        ]
        final = []
        result = Persons.objects().aggregate(query)
        for each in result:
            final.append((each))
        return {"results": final}

class Getone(Resource):
    # @jwt_required()
    def put(self):
        args = request.args.to_dict()
        person = Persons.objects.get(name = 'Karyn Rhodes')
        person.is_deleted = False
        print(person.name)
        person.save()

        return {'results': 'Updated successfully'}, 200


class InsertData(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        person = Persons(**data)
        text = mail_data
        print(data['name'])
        person.content = text.format(supervisor='Smith', name='Watson', sender='Kholi')
        person.save()

        only_one = Persons.objects.get(name="Grace Larson")
        print(type(only_one))
        print(only_one.name)

        # fetch_all = json.loads(Persons.objects().only('name'))
        fetch_all = Persons.objects()
        return {'only_one': json.loads(only_one.to_json()), 'fetch_all': json.loads(fetch_all.to_json())}, 200
