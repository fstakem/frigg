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


class Task(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    text                = Column(Text, nullable=False)

    # Constraints
    job_id              = Column(Integer, ForeignKey('job.id'))

    # Relationships
    job                 = relationship("Job", back_populates="tasks")

    __tablename__ = 'task'
