import re
from flask import Flask, request, jsonify, render_template, redirect, url_for
from xonsh.main import main
import os, sys, docker, re
from mod1 import mod1, clean_chat
# boog_args = "--auto-devices --no-stream --load-in-8bit --chat --listen --extensions openai"

# Instantiate Flask application
app = Flask(__name__)
logs= []    # Create an empty list for storing logs

# Define the route for the base URL
@app.route('/')
def index():
    # Render the index.html template when the base URL is accessed
    return render_template('index.html')
# Define the route for the API
@app.route("/generate", methods=['POST'])
def generate():
    data = request.get_json()
    cleaned_code = clean_chat(data['instruct'])
        
    with open("output.txt", "w") as file:
        file.write(cleaned_code)
    try:
        result = main(args=cleaned_code, stdin=None)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    return jsonify({'status': 'success', 'message': 'Data generated successfully.', 'result': result})

# Define the route for submitting the form
@app.route('/submit', methods=['POST'])
def submit():
    # Get the plain text input of the client
    client_text_entry = request.form.get('client_text_entry')
    # Get the plain text input of the server
    server_text_entry = request.form.get('server_text_entry')
    # TODO: Add code to handle the form submission
    # For now, we will just print the entries
    print("Client entry: ", client_text_entry)
    print("Server entry: ", server_text_entry)
    return redirect(url_for('index'))

# Check if any arguments were passed
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print('Argument passed: ' + arg)
else:
    print('No arguments passed')

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
