#! /usr/bin/python

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer, Text, DateTime, Float 

engine = create_engine('sqlite:////tmp/test.db', echo = False)
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

