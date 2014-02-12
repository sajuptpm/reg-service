
# import uuid
# from sqlalchemy import *

# from sqlalchemy.orm import *
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# RECREATE_DB = False

# class User(Base):
# 	"""
# 	"""
# 	__tablename__ = "user"
# 	id = Column(String(64), primary_key=True)
# 	user_name = Column(String(255), nullable=False)
# 	first_name = Column(String(255), nullable=False)
# 	last_name = Column(String(255), nullable=False)
# 	email = Column(String(255), nullable=False)
# 	country = Column(String(255), nullable=False)
# 	country_code = Column(String(10), nullable=False)
# 	company = Column(String(255), nullable=False)
#         address = Column(String(255), nullable=False)
#         city = Column(String(255), nullable=False)
#         state = Column(String(255), nullable=False)
#         pin = Column(Integer, nullable=False)
#         phone = Column(String(15), nullable=False)
#         external_id = Column(String(255), nullable=False)##user id from keystone
# 	enabled = Column(Boolean, default=False, nullable=False)

# 	def __init__(self, user_name, first_name, last_name, email, country, 
# 			country_code, company, address, city, state, pin, 
# 			phone, external_id, enabled=False):
# 		"""
# 		"""
# 		self.id = uuid.uuid4().hex
# 		self.user_name = user_name 
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.email = email
# 		self.country = country
# 		self.country_code = country_code
# 		self.company = company
# 		self.address = address
# 		self.city = city
# 		self.state = state
# 		self.pin = pin
# 		self.phone = phone
# 		self.external_id = external_id
# 		self.enabled = enabled

# e = create_engine("mysql://root:jio@localhost/jiocloud", echo='debug')
# if RECREATE_DB:
# 	Base.metadata.drop_all(e)
# 	Base.metadata.create_all(e)
# DBSession = scoped_session(sessionmaker(e))








