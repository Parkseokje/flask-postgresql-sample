import os
from os.path import join, dirname, realpath

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
#     os.path.join(BASE_DIR, 'uiti.db'))

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:gowna0928!@localhost:5432/haezoom'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "uiti"
UPLOAD_FOLDER = join(BASE_DIR, 'flask_postgresql_sample/uploads')
MAX_CONTENT_LENGTH = 16 * 1000 * 1000 # 16MB