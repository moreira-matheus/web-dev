# Section 2

<u>Step 1</u>: create and activate a virtual environment:

~~~shell
pip install virtualenv
virtualenv venv
venv\Scripts\activate.bat
~~~

<u>Step 2</u>: install Flask:

~~~shell
pip install Flask
~~~

<u>Step 3</u>: write python code (see `app.py`):

~~~python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
	return 'This is my first Flask app!'

app.run()
~~~

Step 4: run the app:

~~~powershell
python app.py
~~~

***

`templates` folder: .html files

`static` folder: .css files, images etc.

- **Tip**: [PureCSS](https://purecss.io/).
- **Tip**: Format number in [Jinja](https://support.sendwithus.com/jinja/formatting_numbers/).