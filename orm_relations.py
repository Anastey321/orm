from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)
Base = declarative_base()

class Human(Base):
    __tablename__ = "humans"
    # id
    id = Column("human_id", Integer, primary_key=True)
    # name
    name = Column(String(10))
    # age
    age = Column(Integer)

    def getName(self):
        return "Dear, "+self.name
    def nextYearAge(self):
        return 1+self.age

class Hobby(Base):
    __tablename__ = "hobby"
    # id
    id = Column(Integer, primary_key=True)
    # name
    name = Column(String(10))

    human_fk = Column(Integer, ForeignKey('humans.human_id'))
    # link to class
    human = relationship("Human", back_populates = "hobby")


Human.hobbies = relationship("Hobby", back_populates="humans")

Base.metadata.create_all(engine)

