from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    address = Column('address', String(32))
    phone = Column('phone', String(32))

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(32))
    description = Column('description', String(32))
    price = Column('price', Integer)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    customer = Column("customer", String(32))
    product_name = Column("product_name", String(32))
    product_price = Column("product_price", String(32))
    product_description = Column("product_description", String(32))
    amount = Column('amount', String(32))
    date = Column('date', String(32))
    due_date = Column('due_date', String(32))

    def __init__(self, customer, product_name, product_price, product_description, amount, date, due_date):
        self.customer = customer
        self.product_name = product_name
        self.product_price = product_price
        self.product_description = product_description
        self.amount = amount
        self.date = date
        self.due_date = due_date
