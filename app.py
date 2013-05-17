#! /usr/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/create', methods=['GET'])
def create_get():
    return render_template('create_job.html')

@app.route('/create', methods=['POST'])
def create_post():
    return 'Posted to create'

if __name__ == "__main__":
    app.run(debug = True)
