from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base ()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(Integer, nullble=False)


