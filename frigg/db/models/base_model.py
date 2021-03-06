# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.7.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
import json
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import object_mapper


class BaseModel(object):

    created_at      = Column(DateTime, default=datetime.now)
    updated_at      = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        mapper = object_mapper(self)
        items = [(p.key, getattr(self, p.key))
                 for p in [
                    mapper.get_property_by_column(c) for c in mapper.primary_key]]
        return "{0}({1})".format(
            self.__class__.__name__, 
            ', '.join(['{0}={1!r}'.format(*_) for _ in items]))

    def to_dict(self):
        output = {}
        attr = [str(x) for x in dir(self) if x[0] != '_']

        for x in attr:
            output[x] = str(getattr(self, x))

        return output

    def to_json(self):
        output = self.to_dict()

        return json.dumps(output)

