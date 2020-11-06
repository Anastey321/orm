from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import  asyncio


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)
Base = declarative_base()

class Human(Base):
    __tablename__ = "humans"
    id = Column("human_id", Integer, primary_key=True)
    name = Column(String(10))
    age = Column(Integer)

    # link to [Hobby1, Hobby2,... ]
    hobbies = relationship("Hobby", back_populates="human")



class Hobby(Base):
    __tablename__ = "hobby"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    human_fk = Column(Integer, ForeignKey('humans.human_id'))

    # link to class Human
    human = relationship("Human", back_populates = "hobbies")




session = sessionmaker(engine)
open_session = session()


boban = Human(name="Boban", age=21)
boban.hobbies = [ Hobby(name="drinking")]

open_session.add_all(
                        [
                                Human(name="someone", age=17, hobbies= [Hobby(name="h1"), Hobby(name="h2")] ) ,

                                Human(name="someone2", age=18, hobbies= [Hobby(name="h3"), Hobby(name="h4")] )
                        ]
                    )
open_session.commit()


bob = open_session.query(Human).get(9)
print(bob.name)
for hobby in bob.hobbies:
    print(hobby.name)

hobbies = open_session.query(Hobby).filter(Hobby.name=='drinking')
if hobbies:
    for hobby in hobbies:
        print(hobby.human.name)

