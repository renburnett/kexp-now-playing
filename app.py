import requests
import logging
from flask import Flask
frmo flask_ask import Ask, statement

ENDPOINT = 'https://legacy-api.kexp.org/play'
response = requests.get(ENDPOINT)

if response.json()['results'][0]['artist']['name'] != None:
    song_artist_01 = response.json()['results'][0]['artist']['name']
    song_name_01 = response.json()['results'][0]['track']['name']
    song_album_01 = response.json()['results'][0]['release']['name']
    message = "The song currenty playing is {} by {} off of their album {}.".format(song_name_01, song_artist_01, song_album_01)
else:
    if response.json()['results'][1]['artist']['name'] != None:
        song_artist_02 = response.json()['results'][1]['artist']['name']
        song_name_02 = response.json()['results'][1]['track']['name']
        song_album_02 = response.json()['results'][1]['release']['name']
        message = "There is currently an airbreak, however the most recent song prior to the break was {} by {} off of their album {}.".format(song_name_02, song_artist_02, song_album_02)
    else:
        song_artist_03 = response.json()['results'][2]['artist']['name']
        song_name_03 = response.json()['results'][2]['track']['name']
        song_album_03 = response.json()['results'][2]['release']['name']
        message = "There is currently an airbreak, however the most recent song prior to the break was {} by {} off of their album {}.".format(song_name_03, song_artist_03, song_album_03)

print(message)

# r = requests.get(ENDPOINT)
# songs_json = r.json()
# print(songs_json["results"][0]["artist"])

# app = Flask(__name__)
# ask = Ask(app, '/')
# logger = logging.getLogger()

# @ask.launch
# def launch():
#     return stats()

# @ask.intent("StatsIntent")
# def stats():
#     r = requests.get(ENDPOINT)
#     songs_json = r.json()

    # if r.status_code == 200:
    #     repo_name = ENDPOINT.split('/')[-1]
    #     keys = ['stargazers_count', 'subscribers_count', 'forks_count']
    #     stars, watchers, forks = itemgetter(*keys)(repo_json)
    #     speech = "{} has {} stars, {} watchers, and {} forks. " \
    #         .format(repo_name, stars, watchers, forks)
    # else:
    #     message = repo_json['message']
    #     speech = "There was a problem calling the GitHub API: {}.".format(message)

    # logger.info('speech = {}'.format(speech))
    # return statement(speech)

# if __name__ == '__main__':
#     app.run()