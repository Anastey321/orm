from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
Base = declarative_base()

class Human(Base):
    __tablename__= "humans"

    #id
    id = Column("human_id",Integer, primary_key=True)
    # name
    name = Column(String(10))
    # age
    age =Column(Integer)

    def getName(self):
        return "Dear, "+self.name

    def nextYearAge(self):
        return 1+self.age



Base.metadata.create_all(engine)

bob = Human(id =1, name = "Bob", age = 12)

session = sessionmaker(engine)
open_session = session()

open_session.add_all([
    Human( name = "Boba", age = 20),
    Human( name = "Boban", age = 30),])
open_session.commit()

print(bob.getName())