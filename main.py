from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	password = db.Column(db.String(120), nullable=False)

	def __init__(id, username, email, password):
		self.id = id
		self.username
		self.email
		self.password

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		email = request.form.get('email')
		password = request.form.get('password')

		User.query.filter_by(username=username, email=email, password=password)
	return render_template('success.html', message='successfully logged in')

	# https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

@app.route('/signup')
def signup_form():
	return render_template('signup.html')

@app.route('/create/user', methods=['POST', 'GET'])
def create_user():
	if request.method == 'GET':
		return redirect('/')
		
	username = request.form.get('username')
	email = request.form.get('email')
	password = request.form.get('email')

	return render_template('success.html', message='user successfully created')
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=81, debug=True)