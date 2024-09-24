from app import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255), nullable=True)

    def to_json(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "bio": self.bio
        }

class Post(db.Model):
    __tablename__ = "posts"

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_json(self):
        return {
            "post_id":self.post_id,
            "user_id":self.user_id,
            "content":self.content,
            "timestamp":self.timestamp
        }
    
class Comments(db.Model):
    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.post_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_json(self):
        return {
            "comment_id":self.comment_id,
            "post_id":self.post_id,
            "user_id":self.user_id,
            "content":self.content,
            "timestamp":self.timestamp
        }