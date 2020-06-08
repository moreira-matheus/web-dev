#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_bmi(weight, height):
	'''
	Receives weight in kg
	and height in cm.
	Returns the BMI.
	'''
	return weight / ((height/100.) **2)

def analyze_bmi(bmi):
	threshs = [17.0, 18.5, 25.0, 30.0, 35.0, 40.0]
	results = ['Very severely underweight',
	           'Severely underweight',
	           'Underweight', 'Normal',
	           'Overweight', 'Moderately obese',
	           'Severely obese', 'Very severely obese']
	idx = sum([bmi > thresh for thresh in threshs])
	return results[idx]

@app.route('/', methods=['GET', 'POST'])
def welcome():
	args = {}

	if request.method == 'POST':
		
		args['name'] = request.form.get('username')
		args['weight'] = float(request.form.get('userweight'))
		args['height'] = float(request.form.get('userheight'))

		args['bmi'] = calculate_bmi(args['weight'], args['height'])
		args['result'] = analyze_bmi(args['bmi'])

	return render_template('index.html', **args)

app.run()