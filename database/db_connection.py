from mongoengine import register_connection, connect

def create_database():

    connect(db='application-2', alias='db_master')

    # register_connection(db='application-2', alias='db_master', port= 27017, host='localhost')