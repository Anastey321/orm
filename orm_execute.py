from sqlalchemy import create_engine
from sqlalchemy import Integer, String, MetaData, Table, Column


engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

meta = MetaData()

shops = Table(
    'shops',
    meta,
    Column('shop_id',Integer, primary_key=True),
    Column('shop_name', String(10))
)

connection = engine.connect()

# DELETE
rows = connection.execute(  shops.delete().where(shops.c.shop_id==114)  )

# INSERT
rows = [
    {"shop_id":114, "shop_name":"Shop 114"},

]


connection.execute(shops.insert(),    rows   )

# select
rows = connection.execute( shops.select() )

for row in rows:
    print(row)

# select where
rows = connection.execute( shops.select(shops.c.shop_id>100) )
for row in rows:
    print(row)

# update

rows = connection.execute(  shops.update().where(shops.c.shop_id==114).values( shop_name="updated" )  )

print(rows)



