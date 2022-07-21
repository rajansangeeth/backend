from mongoengine import StringField, Document
from datetime import datetime


class LoginActivity(Document):
    email = StringField()
    logged_in_at = datetime.utcnow()

    meta={'db_alias': 'db_master'}
