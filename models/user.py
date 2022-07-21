from mongoengine import StringField, Document, DateTimeField

class Users(Document):
    department = StringField()
    gender = StringField()
    age = StringField()
    id = StringField()
    last_name = StringField()
    first_name = StringField()
    date = StringField()
    country = StringField()
    dob = DateTimeField(default="None")

    meta = {'db_alias': 'db_master'}