from flask import Flask, render_template, request, redirect, url_for
import database
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

# @app.route('/home')
# def home():
# 	return render_template("home.html")


@app.route('/user/<int:id>')
def get_user_route(id):
    user = database.get_user_by_id(id)
    return render_template('user.html', user=user)



@app.route("/sign_in", methods=["POST"])
def get_user():

	uname = request.form["uname"]
	password = request.form["psw"]

	user_id = database.sign_in(uname, password)
	if user_id:
		return redirect(url_for("get_user_route", id=user_id))
	else:
		return render_template("register.html")

@app.route("/register", methods=["POST","GET"])
def register():
	if request.method == "POST":
		username= request.form["email"]
		password = request.form["pws"]
		password_2 = request.form["psw-rpeat"]

		creat_user(username, password, password_2)
		return render_template("home.html")
	else:
		return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)

