#! /usr/bin/python

from flask import Flask, render_template, request 
from forms import JobForm
from models import Job
import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Herp Derpson the third'

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/create', methods=['GET'])
def create_get():
    form = JobForm()
    return render_template('create_job.html', form=form)

@app.route('/create', methods=['POST'])
def create_post():
    form = JobForm(request.form)

    if(form.validate()):
        job = Job(form.data);
        job.save()
        return '%r' % job    
    else:
        return render_template('create_job.html', form=form) 
    
    #save that data
    pass

if __name__ == "__main__":
    app.run(debug = True)
