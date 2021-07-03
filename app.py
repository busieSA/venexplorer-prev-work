from flask import Flask, app
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

#	@app.route('/about')
#	def about():
#		return render_template("about.html")

@app.route('/work')
def work():
	return render_template("work.html")

# work links to catagories



if __name__ == "__main__":
	app.run(debug=True)