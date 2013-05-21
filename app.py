#! /usr/bin/python

from flask import Flask, render_template, request
from forms import JobForm 

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/create', methods=['GET'])
def create_get():
    return render_template('create_job.html', form=form)

@app.route('/create', methods=['POST'])
def create_post():
    print('%r', request)
    form = JobForm(request.form)
    
    if(form.validate()):
        return "It Validated" 
    else:
        return "It didn't validate :("
    
    #save that data
    pass

if __name__ == "__main__":
    app.run(debug = True)
