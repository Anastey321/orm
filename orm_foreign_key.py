from sqlalchemy import create_engine
from sqlalchemy import Integer, String, MetaData, Table, Column, ForeignKey
from sqlalchemy.sql import select

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

meta = MetaData()
meta.create_all(engine)


parent = Table(
    'parent',
    meta,
    Column('parent_id',Integer, primary_key=True),

)

child = Table(
    'child',
    meta,
    Column('child_id',Integer, primary_key=True),
    Column('parent_fk', Integer, ForeignKey('parent.parent_id') ),

)

meta.create_all(engine)

# insert parent+child

# update child

# delete parent


# JOIN
join = parent.join(child, parent.c.parent_id == child.c.parent_fk)

query = select( [ parent, child.c.parent_fk ] ).select_from(join)

connection = engine.connect()

rows = connection.execute(query)

for row in rows:
    print(row)
