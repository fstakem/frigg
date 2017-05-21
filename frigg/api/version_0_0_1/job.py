# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.21.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class Job(Resource):

    def get(self, id):
        return 'job get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class JobList(Resource):

    def get(self):
        return 'Jobs get'
