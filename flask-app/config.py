from datetime import timedelta

AUTH_HOST = 'http://sinatra-app:5001'
MONGO_DB_NAME = 'logger'
MONGO_HOST = 'lcmongo-mongodb-replicaset-0,lcmongo-mongodb-replicaset-1,lcmongo-mongodb-replicaset-2' # set to 'localhost' if running mongo not in container
MONGO_PORT = 27017
SECRET_KEY = 'secret-O^#E#mo4ru'
JWT_EXPIRATION_DELTA = timedelta(seconds=3000000)
