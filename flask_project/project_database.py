from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base #to create new database
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Register(Base):
	__tablename__='register'

	Id = Column(Integer,primary_key = True) # It can be used in another database 
	Name = Column(String(250), nullable = False)#Data should not be NULL
	Surname = Column(String(100), nullable = False)
	Reg_no = Column(String(50), nullable = False)
	Mobile_no = Column(String(10), nullable = False)
	Branch = Column(String(20), nullable = False)


engine = create_engine('sqlite:///BVC.db')
Base.metadata.create_all(engine)
print("Database is created........")
