# core/repositories/in_memory_repository.py

from core.interfaces.repository_interface import RepositoryInterface
from core.entities.post import Post

class InMemoryRepository(RepositoryInterface):
    def __init__(self):
        self.posts = []
        self.next_id = 1

    def get_all_posts(self) -> list[Post]:
        return self.posts

    def get_post_by_id(self, post_id: int) -> Post:
        for post in self.posts:
            if post.id == post_id:
                return post
        return None

    def add_post(self, title: str, content: str) -> Post:
        new_post = Post(self.next_id, title, content)
        self.posts.append(new_post)
        self.next_id += 1
        return new_post
