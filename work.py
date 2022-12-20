from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/contacts.html')
def contacts():
    return render_template('contacts.html')
@app.route('/parser.html')
def parser():
    return render_template('parser.html')
