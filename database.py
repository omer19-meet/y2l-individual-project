from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def query_all():
	all_users = session.query(user).all()
	return all_users

def creat_user(username, password, password_2):
	if password==password_2:
		user1 = User(username = username, password = password)
		session.add(user1)
		session.commit()
	else:
		return "passwordsser' is not definedser' is not defined dosn't match"

def sign_in(uname , pws):
	user_3 = session.query(user).filter_by(username=uname).first()
	if user:
		if user.password == pws:
			return user.id
	else:
		return False


print query_all()