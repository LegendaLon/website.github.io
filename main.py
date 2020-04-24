from flask import Flask, request, redirect
from flask import render_template as render

site = Flask(__name__)

@site.route("/", methods=['GET'])
def index():
	botname = "Чёрный дух"
	data = (botname, __name__)
	return render('index.html', data=data)

@site.route('/set', methods=["POST", 'GET'])
def forwaed(name):
	name = ''
	if name == '':
		name = "User"
	a = "Hello " + name.upper()
	return render('home1.html', a=a)

if __name__ == "__main__":
	site.run(debug=True)