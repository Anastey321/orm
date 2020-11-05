
# shops.update().where(shops.c.shop_id==114).values( shop_name="updated" )
#  update shops set shop_name="updated"  where shop_id==114


from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Integer, Float
from sqlalchemy import select, func, and_, or_, between, union

from sqlalchemy import text #prepared query

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

connection = engine.connect()


meta = MetaData()

customers = Table(
    "customers",
    meta,
    Column("cust_id",String(10), primary_key=True),
    Column("cust_name",String(50)),
    Column("cust_contact",String(50)),
    Column("cust_country",String(50)),
    Column("cust_email", String(50)),
)

vendors = Table(
    "vendors",
    meta,
    Column("vend_id",String(10), primary_key=True),
    Column("vend_name",String(50)),
    Column("vend_contact",String(50)),
    Column("vend_country",String(50))
)

products = Table(
    "products",
    meta,
    Column("prod_id",String(10), primary_key=True),
    Column("prod_name",String(50)),
    Column("prod_price",Float())

)

# select max(prod_price) from products

prepared_query = select([ func.max(products.c.prod_price)  ])
cursor = connection.execute(prepared_query)
print(cursor.fetchall())

# select cust_country from customers
#     where cust_email = 'bob'
# union
# select vend_country from vendors

prepared_query = union( select([customers.c.cust_country]).where(customers.c.cust_email=='bob'), select([vendors.c.vend_country]))
cursor = connection.execute(prepared_query)
print(cursor.fetchall())
