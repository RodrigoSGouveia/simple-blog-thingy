# core/repositories/mongo_repository.py

from core.interfaces.repository_interface import RepositoryInterface
from core.entities.post import Post
from bson.objectid import ObjectId
from app import mongo

class MongoRepository(RepositoryInterface):
    def __init__(self):
        self.collection = mongo.db.posts

    def get_all_posts(self) -> list[Post]:
        posts = self.collection.find()
        return [Post(str(post['_id']), post['title'], post['content']) for post in posts]

    def get_post_by_id(self, post_id: int) -> Post:
        post = self.collection.find_one({'_id': ObjectId(post_id)})
        if post:
            return Post(str(post['_id']), post['title'], post['content'])
        return None

    def add_post(self, title: str, content: str) -> Post:
        result = self.collection.insert_one({'title': title, 'content': content})
        return Post(str(result.inserted_id), title, content)
