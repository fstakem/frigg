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


class School(BaseModel, Base):

     # Properties
    id                  = Column(Integer, primary_key=True)
    name                = Column(String, nullable=False)
    start_date          = Column(Date, nullable=False)
    end_date            = Column(Date)
    degree              = Column(String, nullable=False)
    degree_long         = Column(String)
    major               = Column(String, nullable=False)
    gpa                 = Column(String)
    city                = Column(String)
    graduation_date     = Column(Date)
    attending           = Column(Boolean, default=False, nullable=False)
    activities          = Column(Text)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))

    # Relationships
    person              = relationship("Person", back_populates="schools")

    __tablename__ = 'school'
