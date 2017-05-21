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


class Photo(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    name                = Column(String)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))
    project_id          = Column(Integer, ForeignKey('project.id'))
    post_id             = Column(Integer, ForeignKey('post.id'))

    # Relationships
    person              = relationship("Person", back_populates="photos")
    project             = relationship("Project", back_populates="photos")
    post                = relationship("Post", back_populates="photos")

    __tablename__ = 'photo'
