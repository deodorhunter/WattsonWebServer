from plexapi.myplex import MyPlexAccount




# movies = plex.library.section('Movies')
# # for video in movies.search(unwatched=True):
# #     print(video.title)
# for client in plex.clients():
#     print(client)
#     print(client.title)
#
#
# #cosi ottengo il link da passare indietro
film = plex.library.section('Movies').get('Insidious')
print(str(film.getStreamURL()))
url = str(film.getStreamURL().replace('192-168-1-7.5e76fdcc993f4ad597c0d7fbbd751a8e.plex.direct:32400', '2-35-148-234.5e76fdcc993f4ad597c0d7fbbd751a8e.plex.direct:45633'))
print(url)