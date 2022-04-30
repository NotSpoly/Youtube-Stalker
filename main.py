from lib2to3.pgen2 import driver
import urllib, json
from selenium import webdriver
import time

def look_for_a_new_video():
    api_key = "https://consle.developers.google.com"
    channel_id = "" # the ending of a youtube link 

    base_video_url ="https://www.youtube.com/watch?v="
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urllib.urlopen(url)
    vidID = resp['items'] ['id'] ['videoId']

    video_exits = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_fileo)
        if data['videoId'] != vidID:
            driver = webdriver.Chrome()
            driver.get(base_video_url + vidID)
            video_exits = True

        if video_exits:
            with open('video.json', 'w') as json_file:
                data = {'videoId' : vidID}
                json.dump(data, json_file)


try:
    while True:
        look_for_a_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print("Stopping the process")