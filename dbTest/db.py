from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from dbTest.orm.orms import Base, Product, Order, Client, order_products

engine =  create_engine(
    "postgresql+psycopg2://user:root@localhost:54331/app",
    # "postgresql+psycopg2://user:root@postgres:5432/app",
)

Session = sessionmaker(engine)

with Session.begin() as session:
    product1 = Product(name='SSD', price=123.4)
    product2 = Product(name='Monitor', price=233.4)
    product3 = Product(name='Mouse', price=412.4)
    client1 = Client(name="Akezhan", age= 20)
    client2 = Client(name="Docker", age= 20)
    order1 = Order(client_id = 1)
    order2 = Order(client_id = 2)
    # session.add(product1)
    # session.add(product2)
    # session.add(product3)
    # session.add(client1)
    # session.add(client2)
    # session.add(order1)
    # session.add(order2)



Base.metadata.create_all(engine)
