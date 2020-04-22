from app import app
from flask import Flask, request
from flask import render_template as render
from flask import request, redirect

@app.route("/", methods=['GET'])
def index():
	names = "Чёрный дух"
	username = request.cookies.get('username')
	data = (names, username)
	return render('index.html', data=data)

@app.route("/home", methods=['GET', 'POST'])
def home():
	return render('home.html')

@app.route('/forward/', methods=["POST"])
def forwaed(name):
	a = "Hello" + name
	return render('home1.html', a=a)

def move_forward():
	print("Hello")

if __name__ == "__main__":
	app.run(debug=True)