# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    5.21.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask_restful import Resource


class Post(Resource):

    def get(self, id):
        return 'post get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass


class PostList(Resource):

    def get(self):
        return 'post get'
