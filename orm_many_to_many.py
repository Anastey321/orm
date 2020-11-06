from sqlalchemy import create_engine, Column, String, Integer, and_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)
Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    hotels = relationship('Hotel',secondary = 'bookings')


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    clients = relationship('Client',secondary = 'bookings')

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

Base.metadata.create_all(engine)

# session = sessionmaker(engine)
# open_session = session()

client1 =Client(name = 'Bob')
client2 =Client(name = 'Boba')


hotel1 = Hotel(name ='IBIS')
hotel2 = Hotel(name='Hilton')

# hotel1.clients.append(client1)
# hotel1.clients.append(client2)
# hotel2.clients.append(client1)

client1.hotels.append(hotel1)
client1.hotels.append(hotel2)
client2.hotels.append(hotel1)


session = sessionmaker(engine)
open_session = session()
# open_session.add(client1)
# open_session.add(client2)
# open_session.add(hotel1)
# open_session.add(hotel2)
#
# open_session.commit()


bob  = open_session.query(Client).get(3)
if bob:
    print(bob.name)
    for hotel in bob.hotels:
        print(hotel.name)

