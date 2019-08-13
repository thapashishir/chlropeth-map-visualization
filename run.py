from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def visualization_get():
	return render_template('map.html')
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8088)