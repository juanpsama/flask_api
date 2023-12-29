from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# This must be imported into the main server file
db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    
    #This will act like a List of BlogPost objects attached to each User. 
    #The "author" refers to the author property in the BlogPost class.
    # posts = relationship("BlogPost", back_populates="author")
    # comments = relationship("Comment", back_populates="author")

    def to_dict(self):
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), unique = True)
    description = db.Column(db.Text)
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = relationship('Categories', back_populates= 'product')


class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), unique = True)

    product = relationship('Product', back_populates = 'category') 