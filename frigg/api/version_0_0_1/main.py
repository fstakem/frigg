# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    4.30.17   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint
from flask_restful import Api, Resource, url_for

from frigg.api.version_0_0_1.people import People, PeopleList
from frigg.api.version_0_0_1.job import Job, JobList
from frigg.api.version_0_0_1.link import Link, LinkList
from frigg.api.version_0_0_1.photo import Photo, PhotoList
from frigg.api.version_0_0_1.post import Post, PostList
from frigg.api.version_0_0_1.project import Project, ProjectList
from frigg.api.version_0_0_1.school import School, SchoolList
from frigg.api.version_0_0_1.skill import Skill, SkillList
from frigg.api.version_0_0_1.task import Task, TaskList


app_v0_0_1 = Blueprint('app_v0_0_1', __name__)

@app_v0_0_1.route('/')
def version_hello():
    return 'v0.0.1'

rest_api = Api(app_v0_0_1)

# Basic restful routes
rest_api.add_resource(People, '/people/<int:id>')
rest_api.add_resource(PeopleList, '/people/all')
rest_api.add_resource(Job, '/job/<int:id>')
rest_api.add_resource(JobList, '/job/all')
rest_api.add_resource(Link, '/link/<int:id>')
rest_api.add_resource(LinkList, '/link/all')
rest_api.add_resource(Photo, '/photo/<int:id>')
rest_api.add_resource(PhotoList, '/photo/all')
rest_api.add_resource(Post, '/post/<int:id>')
rest_api.add_resource(PostList, '/post/all')
rest_api.add_resource(Project, '/project/<int:id>')
rest_api.add_resource(ProjectList, '/project/all')
rest_api.add_resource(School, '/school/<int:id>')
rest_api.add_resource(SchoolList, '/school/all')
rest_api.add_resource(Skill, '/skill/<int:id>')
rest_api.add_resource(SkillList, '/skill/all')
rest_api.add_resource(Task, '/task/<int:id>')
rest_api.add_resource(TaskList, '/task/all')

# Web routes
# TODO
# - about
# - projects
# - posts
# - photos
# - resume
# - links