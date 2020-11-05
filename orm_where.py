
# shops.update().where(shops.c.shop_id==114).values( shop_name="updated" )
#  update shops set shop_name="updated"  where shop_id==114


from sqlalchemy import create_engine, String, bindparam, Integer, and_, or_, select, Table, MetaData, Column, asc, desc, between
from sqlalchemy import text #prepared query

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

connection = engine.connect()

"""
select cust_name 
    from customers 
    where 
        (
            trim(cust_contact) = 'John Smith' 
            and  
            trim(cust_country) = 'USA'
        )   
        or 
        trim(cust_country) between  'Austria' and 'Zeland'
    order by   cust_name desc  

"""
meta = MetaData()

customers = Table(
    "customers",
    meta,
    Column("cust_id",String(10), primary_key=True),
    Column("cust_name",String(50)),
    Column("cust_contact",String(50)),
    Column("cust_country",String(50))
)

print(
            or_(
                    and_(customers.c.cust_contact == 'John Smith',   customers.c.cust_country=='USA' ),
                    customers.c.cust_country=='Germany'
               )
       )

prepared_query = select([customers.c.cust_name]).where(
                                                        or_(
                                                                and_(customers.c.cust_contact == 'John Smith',   customers.c.cust_country=='USA' ),
                                                                between(customers.c.cust_country,'Austria','Zeland')
                                                           )
                                                     ).order_by(desc(customers.c.cust_name))

cursor = connection.execute(prepared_query)
print(cursor.fetchall())


# price between 8 - 11

