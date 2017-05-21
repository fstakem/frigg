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


class Post(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    title               = Column(String(200), nullable=False)
    text                = Column(Text)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))

    # Relationships
    person              = relationship("Person", back_populates="posts")
    photos              = relationship("Photo", back_populates="post")

    __tablename__ = 'post'
