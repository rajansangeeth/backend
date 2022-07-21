from mongoengine import StringField, Document

class UploadFile(Document):
    file_name = StringField()
    base64 = StringField()

    meta = {'db_alias': 'db_master'}