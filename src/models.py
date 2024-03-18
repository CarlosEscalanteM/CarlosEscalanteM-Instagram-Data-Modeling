import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False, unique = True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25))    
    email = Column(String(150), nullable=False, unique = True)
    password = Column(String(150), nullable=False, unique = True)
    user_posting = relationship("post", backref="user")

class Follower(Base):
    __tablename__="follower"
    ID = Column(Integer, primary_key=True)
    user_from_id= Column(Integer, ForeignKey("user.id"), primary_key = True)
    user_to_id= Column(Integer, ForeignKey("user.id"), primary_key = True)

class Comment (Base):
    __tablename__="comment"
    ID = Column(Integer, primary_key = True)
    comment_description=Column(String(500))
    author_id= Column(Integer, ForeignKey("user.id"))
    comment_id= Column(Integer, ForeignKey("comment.id"))

class Post (Base):
    __tablename__="post"
    ID = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))
    media = relationship("Media", backref="post")
    comments = relationship("Comment", backref="post")

class Media(Base):
    __tablename__="media"
    ID = Column(Integer, primary_key = True)
    type = (String(25))
    url = (String(150)) #Same string as email/user/password
    post_id = Column(Integer, ForeignKey("post.id"))


  
    def to_dict(self):
        return {}

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e