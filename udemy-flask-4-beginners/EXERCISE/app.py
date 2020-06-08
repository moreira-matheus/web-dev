#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
	name = ''
	food = ''
	if request.method == 'POST' and 'username' in request.form:
		name = request.form.get('username')
		food = request.form.get('userfood')

	return render_template('index.html', name=name, food=food)

#@app.route('/method', methods=['GET', 'POST'])
#def method():
#	if request.method == 'POST':
#		return 'You have used the POST method.'
#	else:
#		return 'I reckon you are probably using a GET request.'

app.run()