import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:220706@localhost/college_db_orm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False