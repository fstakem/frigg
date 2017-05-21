# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.7.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date, Numeric

from frigg.db.models.api import Base
from frigg.db.models.base_model import BaseModel


class Project(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    name                = Column(String(100), nullable=False)
    start_date          = Column(Date)
    end_date            = Column(Date)
    short_description   = Column(Text(500), nullable=False)
    long_description    = Column(Text(1000), nullable=False)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))
    
    # Relationships
    person              = relationship("Person", back_populates="projects")
    skills              = relationship("Skill", back_populates="project")
    links               = relationship("Link", back_populates="project")
    photos              = relationship("Photo", back_populates="project")

    __tablename__ = 'project'
