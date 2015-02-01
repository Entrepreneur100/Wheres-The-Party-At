
from flask import Flask, render_template, request, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from sys import argv
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db = SQLAlchemy(app)

print "WEBPAGE COMPILED!"

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
	print user
	db.session.add(user)
	db.session.commit()
	abort(200)

@app.route('/get_locations')
def handle_get_locations():
	# read the data from the database using sqlite

	# format the records you received into list of dictionaries
	data = []

	users = db.session.query(User).all()

	for user in users:
		data.append({
		'longitude': user.longitude,
		'latitude': user.latitude
		})

	# return the list of dictionaries as json
	return jsonify(locations=data)

def handle_create_db():
	db.create_all()	
	db.session.commit()
	print "OK"

if __name__ == '__main__':
	#handle_create_db()
	app.run(debug = True)
  
  