from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Text,Float,Numeric
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50),nullable=True)
    las_name = Column(String(50),nullable=True)
    user_name = Column(String(50),unique=True)
    password = Column(String(50),nullable=True)
    emai = Column(String(50),nullable=True)
    is_staff = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    orders = relationship('Order', back_populates='user')


    def __repr__(self):
        return self.first_name



class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    price = Column(Numeric(10,2))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='products')

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')

