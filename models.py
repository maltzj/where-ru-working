#! /usr/bin/python

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer, Text, DateTime, Float 
from sqlalchemy import select

engine = create_engine('sqlite:////tmp/test.db', echo = False)
metadata = MetaData(bind = engine)

jobs = Table('jobs', metadata,
            Column('id', Integer, primary_key = True),
            Column('name', String(40), nullable = False),
            Column('email', String(50), nullable = False),
            Column('company', String(50), nullable = False),
            Column('start_date', DateTime, nullable = False),
            Column('end_date', DateTime),
            Column('location', String(50)),
            Column('monthly_pay', Float),
            Column('review', Text)
        )

metadata.create_all(engine)

class Job(object):

    def __init__(self, fields = None):
        self.id = None
        if fields == None:
            pass
        elif hasattr(fields, 'id'):
            #init a the fields based on a database query
            pass
        else:
            #otherwise, initialize fields from the array
            self.name = fields['name']
            self.email = fields['email']
            self.company = fields['company']
            self.start_date = fields['start_date']
            self.end_date = fields['end_date']
            self.location = fields['location']
            self.pay = fields['monthly_pay']
            self.review = fields['review']
            self.id = None
    
    def save(self):
        conn = engine.connect()
        #save the field to the jobs table
        insert = jobs.insert()
        dict = self.__dict__
      
        # If we haven't set id, this is an insert, not update
        if self.id == None:
            del(dict['id'])
        
        conn.execute(insert, dict)
        conn.close()
   
    @classmethod
    def find(id):
        #find by a given id
        pass

    @classmethod
    def find_where(fields):
        #find a job where a given set of fields are the case
        pass

    @classmethod
    def list(self):
        conn = engine.connect()
        select_jobs = select([jobs])
        results = conn.execute(select_jobs)
        return results.fetchall()

        



