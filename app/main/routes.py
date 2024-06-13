# app/main/routes.py
from flask import Blueprint
from app.main.controllers import BlogController

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return BlogController.home()

@main.route('/post/<string:post_id>')
def post(post_id):
    return BlogController.get_post(post_id)

@main.route('/new_post', methods=['GET', 'POST'])
def new_post():
    return BlogController.new_post()
