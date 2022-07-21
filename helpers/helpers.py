import base64

path = 'uploads/'

def convert_and_save(file_name, b64_string):
    file_path = path + file_name
    with open(file_path, "wb") as fh:
        if ',' in b64_string:
            base64_string = b64_string.split(',')[1]
            fh.write(base64.decodebytes(base64_string.encode()))
        else:
            fh.write(base64.decodebytes(b64_string.encode()))
    return file_path

