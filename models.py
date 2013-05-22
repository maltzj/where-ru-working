#! /usr/bin/python

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer, Text, DateTime, Float 

engine = create_engine('sqlite:////tmp/test.db', echo = False)
conn = engine.connect()
metadata = MetaData(bind = engine)

jobs = Table('jobs', metadata,
            Column('id', Integer, primary_key = True),
            Column('name', String(40), nullable = False),
            Column('email', String(50), nullable = False),
            Column('company_name', String(50), nullable = False),
            Column('start_date', DateTime, nullable = False),
            Column('end_date', DateTime),
            Column('location', String(50)),
            Column('pay', Float),
            Column('review', Text)
        )

medatadata.create_all(engine)

class Job(Object):

    def __init__(self, fields = None):
        self.id = None
        if fields == None:
            pass
        elif fields.id:
            #init a the fields based on a database query
            pass
        else:
            #otherwise, initialize fields from the array
            self.name = name
            self.email = email
            self.company_name = company_name
            self.start_date = start_date
            self.end_date = end_date
            self.location = location
            self.pay = pay
            self.review = review
            self.id = None

    
    def save(self):
        #save the field to the jobs table
        insert = jobs.insert()
        dict = self.__dict__
       
        if self.id == None:
            del(dict.id)
        
        conn.execute(insert, dict)
   
    @classmethod
    def find(id):
        #find by a given id
        pass

    @classmethod
    def find_where(fields):
        #find a job where a given set of fields are the case
        pass



