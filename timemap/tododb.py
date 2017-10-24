#!/usr/bin/python3
# -*-coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Numeric, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from task import Task

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()
Base.metadata.create_all(engine)

class TaskRecord(Base):
    __tablename__ = 'tasks'

    id = Column(Integer(), primary_key=True, unique=True)
    name = Column(String(120), index=True, unique=True)
    current_list = Column(String(20), index=True)
    priority = Column(String(1), index=True)
    due_date = Column(DateTime())
    created_date = Column(DateTime(), default=datetime.now)
    updated_date = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

def main(**kwargs):
    pass
    #atask = "(B) 2017-09-26 Hair trim/cut +errands @30min due:2017-10-10 rec:2w"
    #atask = TaskRecord(atask)

if __name__ == '__main__':
    main()