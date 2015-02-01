from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
	return render_template ('home.html')

@app.route('/map')
def themap():
	return render_template('geolocation1.html')


	
if __name__ == '__main__':
    app.run()