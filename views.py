import requests
import sys
import logging
import json

from flask import Flask, render_template, request
app = Flask(__name__)

globalStation = []


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)