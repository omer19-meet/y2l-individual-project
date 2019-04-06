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

def query_user_by_username(uname):
	user_5 = session.query(user).filter_by(username=uname).first()
	return user_5

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

def write_shift(owner, shift_start_date ,start_hour, finish_hour):
	shift_1 = shift(owner=owner, shift_start_date=shift_start_date, start_hour=start_hour, finish_hour=finish_hour)
	check_time =shift_1.total_work_time()
	print(check_time)
	if check_time <= 0:
		return False
	else: 
		session.add(shift_1)
		session.commit()
		return True


def get_shift_by_owner(owner):
	shift_1 = session.query(shift).filter_by(owner=owner).all()
	return shift_1

def get_shift_by_id(id):
	shift_2 = session.query(shift).filter_by(id=id).first()
	return shift_2

def get_shift_by_month(date, owner):
	shiftsss = get_shift_by_owner(owner)
	shifts_new = []
	for i in shiftsss :
		if int(i.start_shift_date_time[5:7]) == int(date[5:7]):
			shifts_new.append(i)
	return shifts_new


def write_shift(owner, shift_start_date ,start_hour, finish_hour):
	shift_1 = shift(owner=owner, shift_start_date=shift_start_date, start_hour=start_hour, finish_hour=finish_hour)
	check_time =shift_1.total_work_time()
	print(check_time)
	if check_time <= 0:
		return False
	else: 
		session.add(shift_1)
		session.commit()
		return True

def delete_shift1(id):
	session.query(shift).filter_by(id=id).delete()
	session.commit()


# write_shift(1, "28/04/2019", "09:00", "17:00")
# creat_user("omer", 211, 211)

# print query_all()