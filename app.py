import json, traceback, click
from flask import Flask, jsonify, url_for, request
from flask_cli import FlaskCLI

JSON_FILE_NAME = 'cv.json'
TEXT_COLOR = '\033[0;34;47m'

app = Flask(__name__)
FlaskCLI(app)

def hadnle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            stack = traceback.format_tb(e.__traceback__)
            response = {'function': func.__name__, 
                        'error': str(e), 
                        'stack': stack}
 
            return jsonify(response)

    wrapper.__name__ = func.__name__
    return wrapper

def load_JSON_file(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        return json.loads(data)

def load_JSON_section_from_file(file_name, section=None):
    data = load_JSON_file(file_name)
    if section:
        return data[section]
    else:
        return data

def color_text(text):
    return f'{TEXT_COLOR}{text}\033[0;37;40m'


def format_JSON_to_string(data, tabs=0):
    string_data = ''

    if type(data) == dict:
        for key in data:
            if (type(data[key]) == dict) or (type(data[key]) == list):
                string_data += tabs * '\t' + color_text(str(key)) + '\n'
                # print(tabs * '\t' + str(key))
                string_data += format_JSON_to_string(data[key], tabs+1)

            else:
                # print(tabs * '\t' + f"{key} - {data[key]}")
                string_data += tabs * '\t' + f"{color_text(key)} - {data[key]}\n"
        
    elif type(data) == list:
        for element in data:
            if (type(element) == dict) or (type(element) == list):
                string_data += format_JSON_to_string(element, tabs+1) + '\n'
                # print()
            else:
                # print(tabs * '\t' + str(element))
                string_data += tabs * '\t' + str(element) + '\n'
    
    return string_data

@app.route("/")
def help():
    print(app.url_map)
    print(url_for('resume_get'))
    print(request.base_url)
    help_map = {
        'Entire CV': request.base_url + 'resume',
        'CV Education CV': request.base_url + 'education',
        'CV Experience CV': request.base_url + 'experience',
        'CV Personal section': request.base_url + 'personal'
    }
    return jsonify(help_map)

@app.route('/resume', methods=['GET'])
@hadnle_exceptions
def resume_get():

    data = load_JSON_section_from_file(JSON_FILE_NAME)
    return jsonify(data)

@app.route('/personal', methods=['GET'])
@hadnle_exceptions
def personal_get():

    data = load_JSON_section_from_file(JSON_FILE_NAME, 'personal')
    return jsonify(data)

@app.route('/experience', methods=['GET'])
@hadnle_exceptions
def experience_get():
    data = load_JSON_section_from_file(JSON_FILE_NAME, 'experience')
    return jsonify(data)

@app.route('/education', methods=['GET'])
@hadnle_exceptions
def education_get():
    data = load_JSON_section_from_file(JSON_FILE_NAME, 'education')
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'error': 'The requested endpoint is not valid'})

@app.cli.command("show-details")
def print_details():
    """Print the entire CV"""
    data = load_JSON_section_from_file(JSON_FILE_NAME)
    print(format_JSON_to_string(data))

@app.cli.command("show-personal-details")
def print_details():
    """Print personal details from CV"""
    data = load_JSON_section_from_file(JSON_FILE_NAME, 'personal')
    print(format_JSON_to_string(data))

@app.cli.command("show-experience-details")
def print_details():
    """Print experience details from CV"""
    data = load_JSON_section_from_file(JSON_FILE_NAME, 'experience')
    print(format_JSON_to_string(data))

@app.cli.command("show-education-details")
def print_details():
    """Print education details from CV"""
    data = load_JSON_section_from_file(JSON_FILE_NAME, 'education')
    print(format_JSON_to_string(data))


if __name__ == '__main__':  
    app.run()