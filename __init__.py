from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

def app_create(**kwargs):
    app.logger.info('app_create()')

def app_update(**kwargs):
    app.logger.info('app_update()')

def app_delete(**kwargs):
    app.logger.info('app_delete()')

class Utils:
    def parse_request_args():
        app.logger.info('parse_request_args()')
        parser = reqparse.RequestParser()
        parser.add_argument('user', required=True, help='User name cannot be blank')
        parser.add_argument('password', required=True, help='Password cannot be blank')
        args = parser.parse_args()
        app.logger.info('args: {args}'.format(args = args))
        return args

class UsersInfo(Resource):
    def post(self):
        app.logger.info('UsersInfo.post()')
        args = Utils.parse_request_args()
        app_create(user=args.user, password=args.password)
        return 201

    def put(self):
        app.logger.info('UsersInfo.put()')
        args = Utils.parse_request_args()
        app_update(user=args.user, password=args.password)
        return 201

    def delete(self):
        app.logger.info('UsersInfo.delete()')
        args = Utils.parse_request_args()
        app_delete(user=args['user'], password=args['password'])
        return 201

api.add_resource(UsersInfo, "/user_info")
if __name__ == '__main__':
    app.run(port='5002', debug=True)