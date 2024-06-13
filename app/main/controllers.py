# app/main/controllers.py

from flask import render_template, request, redirect, url_for
from core import BlogService, MongoRepository

repository = MongoRepository()
blog_service = BlogService(repository)

class BlogController:
    @staticmethod
    def home():
        posts = blog_service.get_all_posts()
        return render_template('index.html', posts=posts)

    @staticmethod
    def get_post(post_id):
        post = blog_service.get_post_by_id(post_id)
        return render_template('post.html', post=post)

    @staticmethod
    def new_post():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            blog_service.add_post(title, content)
            return redirect(url_for('main.home'))
        return render_template('new_post.html')
