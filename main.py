from app import app
from flask import Flask, request, render_template

@app.route("/", methods=['GET'])
def index():
	names = "Legenda Lon"
	return render_template('index.html', n=names)

if __name__ == "__main__":
	app.run(debug=True)