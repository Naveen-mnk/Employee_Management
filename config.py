import os

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@localhost/employee_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")