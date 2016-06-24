"""
This is the web app to connect to the internet and controll the light switch
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello/<name>')
def hello(name='stranger'):
	return render_template('page.html', name = name)

if __name__ == '__main__':
	app.run(debug=True, host ='0.0.0.0')