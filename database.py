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

def query_user_by_id(id):
	user_4 = session.query(user).filter_by(id=id).first()
	return user_4

def creat_user(username, password, password_2):
	if password== password_2:
		user1 = user(username = username, password = password)
		session.add(user1)
		session.commit()
		return "user created succesfully"
	else:
		return "passwords dosn't match"

def sign_in(uname , pws):
	user_3 = session.query(user).filter_by(username=uname).first()
	if user_3:
		if user_3.password == pws:
			return user_3.id
	else:
		return False


print query_all()