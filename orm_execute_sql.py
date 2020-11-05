
# shops.update().where(shops.c.shop_id==114).values( shop_name="updated" )
#  update shops set shop_name="updated"  where shop_id==114


from sqlalchemy import create_engine, String, bindparam, Integer
from sqlalchemy import text #prepared query

engine = create_engine("mysql+pymysql://elko:elko@10.10.64.201/elko", echo=True)

connection = engine.connect()

query="""
    select cust_name 
    from customers 
    where 
        trim(cust_contact) = trim(:contact) 
        and  
        trim(cust_country) = trim(:country)

"""
# query_str => prepared query object
cursor = connection.execute( text(query), contact='   John Smith   ', country='USA')

for row in cursor.fetchall():
    print(row)

 # VS parameters bindings
prepared_query = text(query)
prepared_query = prepared_query.bindparams(
    bindparam("contact", type_ = String),
    bindparam("country", type_ = Integer),

)
# dict

cursor = connection.execute( prepared_query, {
                                                    "contact": '   John Smith   ',
                                                    "country":'10'
                                             }
                             )
for row in cursor.fetchall():
    print(row)

# Products
# vend_id = 'BRS01' and prod_price>8