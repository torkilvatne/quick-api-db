from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    city = Column(String, index=True)
    phone = Column(String, index=True)
    gender = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    postcode = Column(Integer, index=True)

    #marks = relationship("Mark", back_populates="owner")


#class Mark(Base):
#    __tablename__ = "marks"
#
#    id = Column(Integer, primary_key=True, index=True)
#    mark = Column(Integer, index=True)
#    subject = Column(String, index=True)
#    owner_id = Column(Integer, ForeignKey("students.id"))
#
#    owner = relationship("Student", back_populates="marks")