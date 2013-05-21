#! /usr/bin/python

from flask.ext.wtf import Form, TextField, DateField, TextAreaField, validators

class JobForm(Form):
    name = TextField(u'Name ', [validators.Required()])
    email = TextField(u'Email Address', [validators.Required(),
        validators.email()])
    company = TextField(u'Company Name', [validators.Required()])
    monthly_pay = TextField(u'Pay rate (per month)')
    start_date = DateField(u'Start Date', [validators.Required()])
    end_date = DateField(u'End Date')
    review = TextAreaField(u'Review of the company', [validators.Required()])

