from flask_restful import Resource, reqparse
from src.commons.authFunctions import tokenLogin
from src import cache

class authToServer(Resource):
    #DEPRECATED
    def post(self, user, pwd):
        pass
    def post(self):

        post_parser = reqparse.RequestParser()
        post_parser.add_argument('token', required=True, location='json')
        args = post_parser.parse_args()['token']
        print(args)
        plexInstance = cache.get(args)
        print('printing from cache', plexInstance)
        if plexInstance is None:
            plexInstance = tokenLogin(args)
            cache.set(args, plexInstance)
            print('printing new object in cache', cache.get(args))
        return {
            'message': 'logged',
            'error': False,
        }



