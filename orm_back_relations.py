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
    hobbies = relationship("Hobby", backref="human")



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




human = Human(name="John", age=22)

hobby1 = Hobby(name="swimming")
hobby2 = Hobby(name="running")

hobby1.human  = human
hobby2.human  = human



session = sessionmaker(engine)
open_session = session()
open_session.add( human )
open_session.commit()
