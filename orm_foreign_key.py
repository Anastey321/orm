from sqlalchemy import create_engine
from sqlalchemy import Integer, String, MetaData, Table, Column, ForeignKey


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

meta = MetaData()

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

