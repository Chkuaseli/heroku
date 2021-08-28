import os
basedir = os.path.abspath(os.path.dirname(__file__))
# image = os.path.join(basedir,'static/images')
class Config:
    DEBUG = True
    TESTING = True
#   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql://akpisqqwdpsnyz:039341e558ac05f36f2b43ce5cfd2abed4f00c0782fead8317bbe44994a268a7@ec2-54-73-147-133.eu-west-1.compute.amazonaws.com:5432/ddk08pv3hmslrf'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY = 'swisscapital' 
#     # photos 
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
#     DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
