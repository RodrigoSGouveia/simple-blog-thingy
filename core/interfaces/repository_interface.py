# core/interfaces/repository_interface.py

from abc import ABC, abstractmethod
from core.entities.post import Post
from typing import List

class RepositoryInterface(ABC):
    @abstractmethod
    def get_all_posts(self) -> List[Post]:
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: int) -> Post:
        pass

    @abstractmethod
    def add_post(self, title: str, content: str) -> Post:
        pass
