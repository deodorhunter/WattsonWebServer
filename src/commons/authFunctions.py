from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
import requests

def tokenLogin(token):
    baseurl = 'https://192-168-1-7.5e76fdcc993f4ad597c0d7fbbd751a8e.plex.direct:32400'
    # token = 'SsUFBLHa6ZEEgFnm9Uxz'
    plex = PlexServer(baseurl, token)
    print(plex)
    return plex

#   DEPRECATED
#login is done client-side, provide token only
def emailAndPwdLogin(email, pwd):
    account = MyPlexAccount(email, pwd)
    plex = account.resource('DESKTOP-64JOP3E').connect()
    print(plex)
    return plex

def pingServer(token):
    try:
        request = requests.get('http://192.168.1.7:32400/', headers={'X-Plex-Token': token})
        request.raise_for_status()
    except requests.exceptions.HTTPError as httpErr:
        print(httpErr)
    finally:
        return request.status_code
