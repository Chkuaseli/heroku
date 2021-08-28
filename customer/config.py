import os
# from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

basedir = os.path.abspath(os.path.dirname(__file__))
# image = os.path.join(basedir,'static/images')
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres://ksnyytxrrdyvrm:010a847b983afd6ea094180b220031f7d076a3df8b560cec7a65d8a91ec49c8e@ec2-54-159-35-35.compute-1.amazonaws.com:5432/dds3tcmf96mqbe'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY = 'swisscapital' 
#     # photos 
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
#     DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
