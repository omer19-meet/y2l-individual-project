from flask import Flask, render_template, request, redirect, url_for
from database import *
app = Flask(__name__)

@app.route('/')

# home page with a singin form
def hello_world():
    return render_template("home.html")

# @app.route('/home')
# def home():
# 	return render_template("home.html")

# the personal profile of each user.
@app.route('/user/<int:id>')
def query_user_route(id):
    user = query_user_by_id(id)
    return render_template('user.html', user=user)


# takes the users' input from the form at homepage, checks if it's actually exist in the DB.
# if the user exist, send him to his profile, his unquie page.
# if there is no such user, send him to register.
@app.route("/sign_in", methods=["POST"])
def get_user():

	uname = request.form["uname"]
	password = request.form["psw"]

	user_id = sign_in(uname, password)
	print(user_id)
	if user_id:
		return redirect(url_for("query_user_route", id=user_id))
	else:
		return redirect(url_for('register'))

# this rout is for craeting a new acount.
# it takes the users inpunts from "register.html" tamplet and creats a new user object in the DB.
# the "responses" are messages coming from "creat_user()" function supesed to tell the user 
# if the acount was created succesfully or that the passwords doesn't match.
# the responses ARE NOT ACTIVE at the moment because they are cusing to manny bugs. 
@app.route("/register", methods=["POST","GET"])
def register():
	if request.method == "POST":
		username= request.form["email"]
		password = request.form["psw"]
		password_2 = request.form["psw-repeat"]

		print(username, password, password_2)
		# response = creat_user(username, password, password_2)
		creat_user(username, password, password_2)
		# if response== "passwords dosn't match":
		# 	return render_template("register.html",response=response)
		# else:
		return redirect(url_for("hello_world"))
	else:
		return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)

