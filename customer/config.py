import os
# from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

basedir = os.path.abspath(os.path.dirname(__file__))
# image = os.path.join(basedir,'static/images')
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres://edzypmfmnoaqxl:a166de67b2668f379768dbce9889be365ab88607b2c7063ac06736c20d06b48b@ec2-176-34-105-15.eu-west-1.compute.amazonaws.com:5432/d475uh57d2gntk'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY = 'swisscapital' 
#     # photos 
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
#     DROPZONE_ALLOWED_FILE_TYPE = 'image/*'
