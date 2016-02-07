from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('mongodb://hackbrown:hackbrown@ds059135.mongolab.com:59135/hackbrown')
db = client['hackbrown']
coll=db['volunteer_info']

#@app.route("/", methods=['GET', 'PUT'])
#def home():
#	return "Hello World"


@app.route("/", methods=['GET', 'POST'])
def form():
	print('hi')
	print(request)
	print(request.method)
	if request.method == 'POST':
		print("tst")
		name = request.form['name']
		major = request.form['major']


		post = {"major": major,
				"name" : name}
    			

		post_id = coll.insert(post)
		print post_id

		return "You submitted the form!"
	else:
		print("Hello There")
		return render_template('index.html')

if __name__ == "__main__":
    app.run(host='172.18.184.216', debug=True)