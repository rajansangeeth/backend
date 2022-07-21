from mongoengine import StringField, ListField, IntField, DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField
from datetime import datetime

class Week(EmbeddedDocument):
    week = StringField()
    status = StringField()

class Procedure(Document):
    name = StringField()
    plan = EmbeddedDocumentField(Week)
    created_on = DateTimeField(default=datetime.now())
    description = StringField()

    meta = {'db_alias': 'db_master'}
