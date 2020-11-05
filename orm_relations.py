from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)
Base = declarative_base()

class Human(Base):
    __tablename__ = "humans"
    # TABLE COLUMNS
    # id
    id = Column("human_id", Integer, primary_key=True)
    # name
    name = Column(String(10))
    # age
    age = Column(Integer)
    # END TABLE COLUMNS

    # link to [Hobby1, Hobby2,... ]
    hobbies = relationship("Hobby", back_populates="human")



class Hobby(Base):
    __tablename__ = "hobby"

    # TABLE COLUMNS
    # id
    id = Column(Integer, primary_key=True)
    # name
    name = Column(String(10))
    # fk
    human_fk = Column(Integer, ForeignKey('humans.human_id'))
    # END TABLE COLUMNS

    # link to class Human
    human = relationship("Human", back_populates = "hobbies")




session = sessionmaker(engine)
open_session = session()


boban = Human(name="Boban", age=21)
boban.hobbies = [ Hobby(name="drinking")]

open_session.add(boban)
open_session.commit()


bob = open_session.query(Human).get(9)
print(bob.name)
for hobby in bob.hobbies:
    print(hobby.name)

hobbies = open_session.query(Hobby).filter(Hobby.name=='drinking')
if hobbies:
    for hobby in hobbies:
        print(hobby.human.name)

