from sqlalchemy import create_engine, Column, String, Integer, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


session = sessionmaker(engine)
open_session = session()

# open_session.query(Human)  = select ...from Human

humans = open_session.query(Human).all()
for human in humans:
    print(human.getName(), 'yout next year age will be', human.nextYearAge())

# get first row
first_human = open_session.query(Human).first()
print(first_human.name)

# get by id
# select * from humans where human_id = 2
human2 = open_session.query(Human).get(2)
print(human2.name)



# open_session.query(Human) !!! commit  = update ...from Human
boba = open_session.query(Human).get(2)
boba.age = boba.nextYearAge()

open_session.commit()

for human in open_session.query(Human).all():
    human.age = human.nextYearAge()


open_session.commit()

# open_session.query(Human).delete()  = delete ...from Human

# delete by object
boba = open_session.query(Human).get(3)
if boba:
    open_session.delete(boba)
    open_session.commit()

    print(boba.nextYearAge())

# delete all()
open_session.query(Human).delete()


# delete by filter
open_session.query(Human).filter(and_(Human.age>20, Human.age<15)).delete()

# filter
humans = open_session.query(Human).filter(and_(Human.age>20, Human.age<15))
for human in humans:
    print(human.name)