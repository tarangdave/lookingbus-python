import requests
import sys
import logging
import json
import pyrebase
import datastoreHelper as ds

from flask import Flask, render_template, request
app = Flask(__name__)

globalStation = []

config = {
  "apiKey": "AIzaSyBcTW0gFNsGfU91lIb_7WCX1FPjLQyBnIA",
  "authDomain": "lookingbus-237103.firebaseapp.com",
  "databaseURL": "https://lookingbus-237103.firebaseio.com",
  "storageBucket": "lookingbus-237103.appspot.com"
}

firebase = pyrebase.initialize_app(config)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/admin")
def admin():
	return render_template("admin.html")

@app.route("/signup", methods=["POST"])
def signup():
	username = request.form['username']
	password = request.form['password']

	# db = firebase.database()
	# data = {
	# 	"username": username,
	# 	"password": password
	# }

	ds.run_quickstart(username, password)

	# db.child("users").push(data)

	return json.dumps({"status": "success"})

@app.route("/login", methods=["POST"])
def login():
	username = request.form['username']
	password = request.form['password']

	# db = firebase.database()

	# all_users = db.child("users").get()
	# for user in all_users.each():
	# 	myObj = user.val()
	# 	if myObj["username"] == username and myObj["password"] == password:
	# 		return json.dumps({"status":"success"})

	if ds.log_me_in(username, password):
		return json.dumps({"status":"success"})

	return json.dumps({"status": "Invalid Credentials"})
	
@app.route("/table", methods=["GET"])
def table():
	# db = firebase.database()

	# resList = []

	# all_users = db.child("users").get()
	# for user in all_users.each():
	# 	res = {}
	# 	res = user.key(), user.val()["username"], user.val()["password"]
	# 	resList.append(res)
	all_users = ds.get_me_list()


	return json.dumps(all_users)

@app.route("/delete", methods=["GET"])
def delete():
	userid = request.args.get("userid")
	# print(userid)

	# db = firebase.database()

	# db.child("users").child(userid).remove()
	ds.delete_me(userid)

	return json.dumps({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)