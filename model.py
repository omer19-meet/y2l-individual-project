from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# from werkzeug.security import check_password_hash, generate_password_hash


class user(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username  = Column(String)
    password  = Column(String)


























    # def __init__(self, username,name,password):
    #     self.username       = username
    #     self.set_password(password)
    #     self.name           = name

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    # def __repr__(self):
    #     return 'User %d %s' % (self.id, self.username)


    # def __repr__(self):
    #     return 'Journey %d %s' % (self.id, self.title)

