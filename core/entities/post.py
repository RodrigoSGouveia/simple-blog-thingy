# core/entities/post.py



class Post:
    def __init__(self, id: str, title: str, content: str):
        self.title = title
        self.content = content
        self.id = id
