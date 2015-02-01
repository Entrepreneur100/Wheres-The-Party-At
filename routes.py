from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
	return render_template ('home.html')

@app.route('/map')
def themap():
	return app.send_staticc_file(os.path.join('geolocation1.html', templates))


@app.route('/get_locations')
def get_locations(pos):
	pass

# @app.route('/send_locations') #look in flask docs for post requests


	
if __name__ == '__main__':
    app.run()