
from flask import Flask, render_template, request, abort, jsonify
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


# @app.route('/')
def home():
	return render_template ('home.html')

class User(db.Model):

	__tablename__ = 'users'
	identity = db.Column(db.String, primary_key = True)
	longitude = db.Column(db.String, primary_key=True)
	latitude = db.Column(db.String, primary_key=True)
	timestamp = db.Column(db.String, primary_key=True)

	def __init__(self, identity=None, longitude=None, latitude=None, timestamp=None):
		self.identity = identity
		self.longitude = longitude
		self.latitude = latitude
		self.timestamp = timestamp

@app.route('/')
def themap():
	return render_template('geolocation1.html')

@app.route('/send_location', methods=['POST'])
def handle_send_location():
	data = {
	'identity' : request.form['identity'],
	'longitude' : request.form['longitude'],
	'latitude' : request.form['latitude'],
	'timestamp' : request.form['timestamp']
	}

	# write the data to the database using sqlite
	user = User(id = request.form['id'], longitude = request.form['long'], latitude = request.form['lat'], timestamp = request.form['timestamp'])



	abort(401)

@app.route('/get_location')
def handle_get_location():
  # read the data from the database using sqlite

  # format the records you received into list of dictionaries
  data = []

  data.append({
      'longitude': 8.0,
      'latitude': 0.9,
    })

  # return the list of dictionaries as json
  return jsonify(locations=data)



  
if __name__ == '__main__':
    app.run(debug = True)
  
  