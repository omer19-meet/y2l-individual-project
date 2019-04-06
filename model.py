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

# the shifts of every user:
class shift(Base):

    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True)
    owner = Column(Integer)
    shift_start_date = Column(String)
    start_hour = Column(String)
    finish_hour = Column(String)



    def total_work_time(self):
        minutes_1 = float(self.start_hour[3:5])
        minutes_2 = float(self.finish_hour[3:5])
        hours_1 = float(self.start_hour[0:2])
        hours_2 = float(self.finish_hour[0:2])
        print(minutes_1)
        print(minutes_2)
        print(hours_1)
        print(hours_2)
        total_min = (minutes_2-minutes_1)/60
        total_hours = hours_2-hours_1
        total_hours += total_min
        return total_hours

# def register():
#     if request.method == "POST":
#         username= request.form["email"]
#         password = request.form["pws"]
#         password_2 = request.form["psw-rpeat"]

#         creat_user(username, password, password_2)
#         return render_template("home.html")
#     else:
#         return render_template("register.html")


























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

