# CV API code challenge

## Requirement
As a JSON REST API with endpoints GET /personal, GET /experience, GET /education, ...
As a Flask CLI command that prints the data to the console

## How to setup
### Clone the code locally
Use `git clone ...` to synchronize the project locally 

### Create the virtual environment
Open a terminal, navigate to the project directory and create a virtual environment
`python -m venv env`

### Activate the environment
`env\Scripts\Activate` for windows systems
`source env/bin/activate` for unix systems

### Install dependencies
`pip install -r Requirements.txt`

### Set the flask app in environment variables
`set FLASK_APP=app.py` for windows systems
`export FLASK_APP=app.py` for unix systems

## How to use it
Create a cv.json file with minimum template as this one:
`{education, experience, resume}`
In each section you can add whatever data you feel necessary.
There could be more sections than those 3 but those are mandatory.

### REST API
Launch the flask web server by running `flask run` command. Then navigate to [the api](http://127.0.0.1:5000) with your favourite web browser.

There are defined 5 endpoints:
+   /               -   will show a map of the API
+   /resume         -   Will show the whole CV
+   /education      -   Will bring the education section from the CV
+   /experience     -   Will bring the experience section from the CV
+   /personal       -   Will bring the personal section from the CV

### Comand line interface
Basically, running `flask --help` will show the registered commands
They are similarry to the REST API
+   show-details             Print the entire CV
+   show-education-details   Print education details from CV
+   show-experience-details  Print experience details from CV
+   show-personal-details    Print personal details from CV

