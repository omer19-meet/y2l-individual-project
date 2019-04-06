from flask import Flask, render_template, request, redirect, url_for, session as login_session
from database import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdasfsad'
@app.route('/', methods = ['GET', 'POST'])

# home page with a singin form
def hello_world():
	if request.method == 'GET':
   		return render_template("home.html")

	else:
		uname = request.form["uname"]
		password = request.form["psw"]

		user_id = sign_in(uname, password)
		print(user_id)
		if user_id:
			login_session['username'] = uname
			return redirect(url_for("query_user_route", id=user_id))
		else:
			error ="Password or user doesn't match. Try to creat a new account (blue button). Forgot password curently inactive"
			return render_template("home.html", error = error)

@app.route('/user/<int:id>')
def query_user_route(id):
    user = query_user_by_id(id)
    all_shifts = get_shift_by_owner(owner=id)
    return render_template('user.html', user=user, all_shifts=all_shifts)


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
@app.route('/logout')
def logout():
	login_session.pop['username']
	return redirect(url_for('hello_world'))
@app.route("/add_shift", methods=["POST","GET"])
def add_shift():
	if 'username' in login_session:
		username = login_session['username']
		error = "some digits are missing. please make sure to fill all fields properly. dont forget to use AM-PM"
		if request.method == "POST":
			owner = query_user_by_username(username)
			eprove = "new shift added succesfully"
			i_d = owner.id
			date_start = request.form["date_start"]
			time_start = request.form["time_start"]
			time_finish = request.form["time_finish"]
			# print(date_start)
			# print(time_start)
			# print(time_finish)
			if len(str(date_start)) < 9 :
				# print(date_start)
				# print(len(date_start))
				return render_template("new_shift.html", error=error)
			if len(str(time_start))< 5:
				# print(time_start)
				# print(len(time_start))
				return render_template("new_shift.html", error=error)
			if len(str(time_finish)) < 5:
				# print(time_finish)
				# print(len(time_finish))
				return render_template("new_shift.html", error=error)		
			
			if write_shift(owner=i_d, shift_start_date=date_start, start_hour=time_start, finish_hour=time_finish) == True:

				return redirect(url_for("query_user_route", eprove=eprove , id = query_user_by_username(username).id))
			
			return render_template("new_shift.html", error = "you cant go back in time")
		else:
			return render_template('new_shift.html')
	else:
		print("error")
		return redirect(url_for('hello_world'))

@app.route("/delete_shift", methods=["POST","GET"])
def delete_shift():
	if 'username' in login_session:
		username = login_session['username']
		if request.method == "POST":
			
			eprove = "new shift added succesfully"
			i_d = request.form["id_shift"]
			delete_shift1(id=i_d)
			return redirect(url_for("query_user_route", eprove=eprove , id = query_user_by_username(username).id))
			

		else:
			
			return render_template('delete_shift.html')
	else:
		return redirect(url_for("hello_world"))


		

if __name__ == '__main__':
    app.run(debug=True)

