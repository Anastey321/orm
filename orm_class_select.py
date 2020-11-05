from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
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


# open_session.query(Human).all()  = select ...from Human
# open_session.query(Human).update()  = update ...from Human
# open_session.query(Human).delete()  = delete ...from Human
