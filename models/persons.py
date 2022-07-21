from mongoengine import Document, IntField, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField, DateTimeField, BooleanField, DictField

class Location(EmbeddedDocument):
    country = StringField()
    address = StringField()


class Company(EmbeddedDocument):
    title = StringField()
    email = StringField()
    phone = StringField()
    location = EmbeddedDocumentField(Location)


class Persons(Document):
    index = IntField()
    name = StringField()
    isActive = BooleanField(default=False)
    registered = DateTimeField()
    age = IntField()
    gender = StringField()
    eyeColor = StringField()
    favoriteFruit = StringField()
    tags = ListField()
    company = EmbeddedDocumentField(Company)
    is_deleted = BooleanField()
    content = StringField()

    meta = {'db_alias': 'db_master'}