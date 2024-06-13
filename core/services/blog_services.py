# core/services/blog_service.py

from core.entities.post import Post
from core.interfaces.repository_interface import RepositoryInterface

class BlogService:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_all_posts(self) -> list[Post]:
        return self.repository.get_all_posts()

    def get_post_by_id(self, post_id: int) -> Post:
        return self.repository.get_post_by_id(post_id)

    def add_post(self, title: str, content: str) -> Post:
        return self.repository.add_post(title, content)