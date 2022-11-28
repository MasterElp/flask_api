from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

def app_create(**kwargs):
    pass

def app_update(**kwargs):
    pass

def app_delete(**kwargs):
    pass

def parse_request_args():
    parser = reqparse.RequestParser()
    parser.add_argument('user', required=True, help='User name cannot be blank')
    parser.add_argument('password', required=True, help='Password cannot be blank')
    args = parser.parse_args()
    return args

class UsersInfo(Resource):
    def post(self):
        args = parse_request_args()
        app_create(user=args['user'], password=args['password'])
        return {'command': 'post', 'user': args['user'], 'password': args['password']}, 201

    def put(self):
        args = parse_request_args()
        app_update(user=args['user'], password=args['password'])
        return {'command': 'put', 'user': args['user'], 'password': args['password']}, 201

    def delete(self):
        args = parse_request_args()
        app_delete(user=args['user'], password=args['password'])
        return {'command': 'delete', 'user': args['user'], 'password': args['password']}, 201

api.add_resource(UsersInfo, "/user_info")
if __name__ == '__main__':
    app.run(port='5002', debug=True)