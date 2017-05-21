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


class Skill(BaseModel, Base):

    # Properties
    id                  = Column(Integer, primary_key=True)
    name                = Column(String, nullable=False)
    description         = Column(Text)
    category            = Column(String)
    currently_using     = Column(Boolean, default=False)
    last_used           = Column(Date)
    skill_level         = Column(Integer)

    # Constraints
    person_id           = Column(Integer, ForeignKey('person.id'))
    project_id          = Column(Integer, ForeignKey('project.id'))

    # Relationships
    person              = relationship("Person", back_populates="skills")
    project             = relationship("Project", back_populates="skills")

    __tablename__ = 'skill'
