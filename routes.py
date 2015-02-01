from flask import Flask, render_template, request, abort, jsonify
app = Flask(__name__)

# db = SQLAlchemy(app)


# @app.route('/')
# def home():
#   return render_template ('home.html')

@app.route('/')
def themap():
  return render_template('geolocation1.html')

@app.route('/send_location', methods=['POST'])
def handle_send_location():
  data = {
    'id' : request.form['id'],
    'long' : request.form['long'],
    'lat' : request.form['lat'],
    'timestamp' : request.form['timestamp']
  }

  # write the data to the database using sqlite

  abort(401)

@app.route('/get_location')
def handle_get_location():
  # read the data from the database using sqlite

  # format the records you received into list of dictionaries
  data = []

  data.append({
      'long': 8.0,
      'lat': 0.9,
    })

  # return the list of dictionaries as json
  return jsonify(locations=data)



  
if __name__ == '__main__':
    app.run(debug = True)
  
  