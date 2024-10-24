from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class CustomerRepository:
    def __init__(self):
        engine = create_engine('sqlite:///example.db')
        declarative_base().metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create_customer(self):
        new_user = User(name="Alice", age=30)
        self.session.add(new_user)
        self.session.commit()
