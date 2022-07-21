from flask import Request
from models.upload import UploadFile
from flask_restful import Resource
from flask import request
from helpers.helpers import convert_and_save
import PyPDF2 as pd
from helpers.helpers import path

class Upload(Resource):
    def post(self):
        data = request.get_json()
        file = UploadFile(**data)
        convert_and_save(data['file_name'], data['base64'])
        file.save()

        return {'result': 'success'}

    def get(self):
        file = 'D://sample.pdf'
        data = pd.PdfFileReader(file)
        print(data.getNumPages())
        page1 = data.getPage(0)
        page2 = data.getPage(1)
        result = page1.mergePage(page2)
        # print(result)
        text = data.getPage(0).rotateClockwise(90).extractText()
        # text = text.rotateClockwise(90)
        file_path = path + 'sample.txt'

        with open(file_path, 'w') as fh:
            fh.write(text)

        return {'result': 'success'}