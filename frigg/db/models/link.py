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
from sqlalchemy_utils import URLType

from frigg.db.models.api import Base
from frigg.db.models.base_model import BaseModel


class Link(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    url                 = Column(URLType, nullable=False)
    text                = Column(String, nullable=False)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))
    project_id          = Column(Integer, ForeignKey('project.id'))

    # Relationships
    person              = relationship("Person", back_populates="links")
    project             = relationship("Project", back_populates="links")

    __tablename__ = 'link'
