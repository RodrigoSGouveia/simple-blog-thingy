import os

class Config:
    SECRET_KEY = os.environ.get('PYTHON_SIMPLE_BLOG_SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # You can use any database URI
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGODB_URI = os.environ.get('MONGODB_URI') or 'mongodb://localhost:27017/mymongo'  # Replace 'mydatabase' with your database name
