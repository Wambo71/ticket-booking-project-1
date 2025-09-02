from sqlalchemy import Integer, Column, String , DateTime , ForeignKey,create_engine
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
import datetime

Base = declarative_base ()

engine = create_engine("sqlite:///booking.db")
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
session=session()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)

    tickets = relationship("Ticket", back_populates="user")


class Event(Base): 
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    capacity = Column(Integer, nullable=False)

    tickets = relationship("Ticket", back_populates="event")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id")) 
    event_id = Column(Integer, ForeignKey("events.id"))
    booked_at = Column(DateTime, default=datetime.datetime.utcnow) 

    event = relationship("Event",back_populates="tickets")  
    user = relationship("User",back_populates="tickets")

    
# ✅ Create tables after models are defined
Base.metadata.create_all(engine)