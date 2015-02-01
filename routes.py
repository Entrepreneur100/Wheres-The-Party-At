
from flask import Flask, render_template, request, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sys import argv
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db = SQLAlchemy(app)

print ('WEBPAGE COMPILED!')

# @app.route('/')
def home():
	return render_template ('home.html')

class User(db.Model):

	__tablename__ = 'users'
	identity = db.Column(db.String, primary_key = True)
	longitude = db.Column(db.Float, primary_key=True)
	latitude = db.Column(db.Float, primary_key=True)
	timestamp = db.Column(db.Float, primary_key=True)

	def __init__(self, identity, longitude, latitude, timestamp):
		self.identity = identity
		self.longitude = longitude
		self.latitude = latitude
		self.timestamp = timestamp

	def __repr__(self):
		return '<USER %r>' % (self.identity)

@app.route('/')
def themap():
	return render_template('geolocation1.html')

@app.route('/send_location', methods=['POST'])
def handle_send_location():
	data = {
	'identity' : request.form['identity'],
	'longitude' : request.form['longitude'],
	'latitude' : request.form['latitude'],
	'timestamp' : time.time()
	}

	# write the data to the database using sqlite
	user = User(identity = data['identity'], longitude = data['longitude'], latitude = data['latitude'], timestamp = data['timestamp'])
	#replace????????????????
	#user_old = db.session.query(User).filter_by(identity = data['identity']).first()
	# user_old = db.session.query(User).filter_by(True).first()
	# print ('##############################################', user_old)
	# db.session.delete(user_old)
	db.session.query(User).filter(User.identity == data['identity']).delete(synchronize_session = 'False')
	db.session.add(user)
	db.session.commit()

@app.route('/get_locations')
def handle_get_locations():
	# read the data from the database using sqlite

	# format the records you received into list of dictionaries
	data = []

	users = db.session.query(User).all()
	# Not Filter ????????????????????????
	#users = db.session.query(User).filter_by((timestamp - time.time()) < 30)

	for user in users:
		print time.time()
		data.append({
		'longitude': user.longitude,
		'latitude': user.latitude,
		'ID': user.identity
		})

	# return the list of dictionaries as json
	return jsonify(locations=data)

def handle_create_db():
	db.create_all()	
	db.session.commit()

if __name__ == '__main__':
	#handle_create_db()
	app.run(debug = True)
  
  