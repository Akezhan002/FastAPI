from __future__ import annotations

from sqlalchemy import Column, VARCHAR, Float
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from typing import List


class Base(DeclarativeBase):
    pass


order_products = Table(
    "order_products",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
)


class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(VARCHAR(255))
    price = Column(Float)
    orders: Mapped[List[Order]] = relationship(
        secondary=order_products, back_populates="products"
    )


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    age = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id = Column(Integer)
    products: Mapped[List[Product]] = relationship(
        secondary=order_products, back_populates="orders"
    )
