from mongoengine import StringField, IntField, Document, BooleanField, DateTimeField
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash


class Signup(Document):
    first_name = StringField()
    last_name = StringField()
    password = StringField()
    age = IntField()
    email = StringField()
    dob = DateTimeField(default="None")
    created_on = datetime.utcnow()
    category = StringField(default = 'Non-Prime')
    is_deleted = BooleanField(default = False)

    meta={'db_alias':'db_master'}

    def hash_pwd(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_pwd(self,password):
        return check_password_hash(self.password, password)
