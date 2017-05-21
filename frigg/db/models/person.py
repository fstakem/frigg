# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.7.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric, Text

from frigg.db.models.api import Base
from frigg.db.models.base_model import BaseModel


class Person(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    first_name          = Column(String(100), nullable=False)
    last_name           = Column(String(100), nullable=False)
    username            = Column(String(100), nullable=False)
    title               = Column(String(100))
    about_me            = Column(Text(500))
    resume_objective    = Column(Text(200))
    professional_title  = Column(String(100))

    # Constraints

    # Relationships
    skills              = relationship("Skill", back_populates="person")
    links               = relationship("Link", back_populates="person")
    jobs                = relationship("Job", back_populates="person")
    posts               = relationship("Post", back_populates="person")
    projects            = relationship("Project", back_populates="person")
    photos              = relationship("Photo", back_populates="person")
    schools             = relationship("School", back_populates="person")

    __tablename__ = 'person'
