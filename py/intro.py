from flask import Flask, render_template, request, redirect, url_for
import os, sys, docker, json, argparse, xonsh

# declarations
app = Flask(__name__)
logs= []
vargs = argparse.ArgumentParser()

# Load the templates
@app.route('/')
def index():
    return render_template('index.html')

# Route for submitting the form
@app.route('/submit', methods=['POST'])
def submit():
    # Get the CLI args of the client in the form of a request
    client_cli_entry = request.form.get('client_cli_entry')
    logs.append(client_cli_entry)
    
# Check if the number of arguments passed is valid  (1 or 2 only)
if len(sys.argv) > 1:
  for arg in sys.argv[1:]:
      # Handle extra arguments
      vargs.add_argument("echo", help="echo the string you use here")
      vargs.add_argument(arg)
      sys.argv.remove(arg)        
elif (sys.argv[1] != None):
  print(f'Init script name: {sys.argv[0]}')
  print('additional parameters passed: ' + (sys.argv[1:]))
else:
  print('No arguments passed')
  exit()
  
# Parse the argument
args = vargs.parse_args()
for arg in args:
  print(arg)  

"""
This file is a Flask web application that accepts command-line arguments and logs them. It also provides a web interface for submitting additional entries. Here are its key functions:

index()
: This function is mapped to the root URL ("/") of the web application. When a user navigates to the root URL, the server responds by rendering the 'index.html' template.

submit()
: This function is mapped to the "/submit" URL and is designed to handle POST requests. When a form is submitted on the client side, the server retrieves the 'client_cli_entry' from the form data and appends it to the 'logs' list.

The script also checks the command-line arguments passed when the script is run. If there are more than one arguments, it adds them to the argument parser and removes them from the original list. If there is exactly one argument, it prints the script name and the argument. If no arguments are passed, it prints a message and exits the script.

After parsing the arguments, it prints each argument.
"""