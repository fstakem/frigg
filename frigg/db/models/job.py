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


class Job(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    title               = Column(String(100), nullable=False)
    title_long          = Column(String(100))
    company             = Column(String(100))
    city                = Column(String(100), nullable=False)
    state               = Column(String(100), nullable=False)
    start_date          = Column(Date, nullable=False)
    end_date            = Column(Date)
    current_job         = Column(Boolean, default=False, nullable=False)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))

    # Relationships
    person              = relationship("Person", back_populates="jobs")
    tasks               = relationship("Task", back_populates="job")
    
    __tablename__ = 'job'
