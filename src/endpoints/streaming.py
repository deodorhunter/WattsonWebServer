from flask_restful import Resource, reqparse
from src import cache
from src.commons.authFunctions import pingServer, tokenLogin
import json
'''
    things we'll need:
    1. after we send the streaming url back, we should have current video info, such as key
'''


class Streaming(Resource):

    #need to make my own search function, use json/xml to get librarySection and title, then get url via plexAPI
    #EASIER: you get part of the traffic from onDeck(), which has meta key
    #also accept params: librarySectionTitle="Movies" type="movie" title="Avengers: Endgame"
    def get(self):
        get_parser = reqparse.RequestParser()
        get_parser.add_argument('title', required=True, location='args')
        get_parser.add_argument('librarySectionTitle', required=True, location='args')
        get_parser.add_argument('type', required=False, location='args')
        get_parser.add_argument('X-Plex-Token', required=True, location='headers')
        token = get_parser.parse_args()['X-Plex-Token']
        librarySectionTitle = get_parser.parse_args()['librarySectionTitle']
        title = get_parser.parse_args()['title']
        if pingServer(token) is 200:
            plexInstance = cache.get(token)
            if plexInstance is None:
                plexInstance = tokenLogin(token)
                cache.set(token, plexInstance)
            client = plexInstance.client('Chrome')
            print(client)
            film = plexInstance.library.section(librarySectionTitle).get(title)
            print(str(film.getStreamURL()))
            url = str(film.getStreamURL().replace('192-168-1-7.5e76fdcc993f4ad597c0d7fbbd751a8e.plex.direct:32400',
                                                  '37-116-129-105.5e76fdcc993f4ad597c0d7fbbd751a8e.plex.direct:45633'))
            print(film)
            print(film.session)
            print(film.sessionKey)
            print(film.transcodeSessions)
            return url
        elif pingServer(token) is 401:
            return {
                'message': 'Unauthorized',
                'error': 401
            }



