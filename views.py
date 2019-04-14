import requests
import sys
import logging
import json
import pyrebase

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

@app.route("/signup", methods=["POST"])
def signup():
	username = request.form['username']
	password = request.form['password']

	db = firebase.database()
	data = {
		"username": username,
		"password": password
	}

	db.child("users").push(data)

	return json.dumps({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True)