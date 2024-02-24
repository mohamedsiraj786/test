import os
from flask import Flask, jsonify, request, render_template, redirect, url_for,session

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

@app.route('/https://easy-erin-moose-tam.cyclic.app/')
def index():
      return render_template('index.html')
  

if __name__ == "__main__":
    app.run(debug=True)
