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
countries = Table(
    'countries',
    meta,
    Column('country_name', String(10), primary_key=True),

)


meta.create_all(engine)


# INSERT INTO shops (shop_id, shop_name) VALUES (:shop_id, :shop_name)
insert = shops.insert().values( shop_id=222,  shop_name="Just shop")


print(str(insert))
print( insert.compile().params )

# execute
connection = engine.connect()
result = connection.execute(insert)

print(result)