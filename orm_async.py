from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey,select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession



Base = declarative_base()

class Human(Base):
    __tablename__ = "humans"
    id = Column( "human_id", Integer, primary_key=True)
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




async def create_tables():
    engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)

    async  with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)



    async with AsyncSession(engine) as session:
        async with session.begin():

            human = Human(name="Human", age= 0)
            human.hobbies = [ Hobby(name="thinking")]
            session.add(human)

            # await session.commit()



async def select_Humans():
    engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)

    async with AsyncSession(engine) as session:
        async with session.begin():
            humans = await session.execute(select(Human))
            for human in humans:
                print(human)


async def select_Hobby():
    engine = create_async_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=False)

    async with AsyncSession(engine) as session:
        async with session.begin():
            hobbies = await session.execute(select(Hobby))
            for hobby in hobbies:
                print(hobby)


# drop create table
loop = asyncio.get_event_loop()
loop.run_until_complete(create_tables())


loop = asyncio.get_event_loop()
loop.run_until_complete( asyncio.wait([  select_Humans(), select_Hobby() ]) )
print('Finish')