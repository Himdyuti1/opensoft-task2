from flask import Flask

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Himdyuti1@localhost/test'

from app import views