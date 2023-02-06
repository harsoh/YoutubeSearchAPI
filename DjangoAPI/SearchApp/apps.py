from django.apps import AppConfig
import time
import threading
import requests
import psycopg2

keys = ['AIzaSyBg_iq5CBc7cKvG6FKl9Hq4JaPHtU5px68', 'AIzaSyAPdAqBNQRrPaDN6JUVh_zMLzhzFzjcoos', 'AIzaSyAzgZ75tVnrVzLbl1EKQMFvjdVGXP1A77M']

def http_call_async():
    idx = 0
    while(1):
        time.sleep(10)
        search_url = 'https://www.googleapis.com/youtube/v3/search'

        params = {
            'part' : 'snippet',
            'q' : 'football',
            'type' : 'video',
            'order' : 'date',
            'publishedAfter' : '2023-02-02T00:00:00Z',
            'maxresults' : 50,
            'key' : keys[idx]
        }

        r = requests.get(search_url, params=params)
        if r.status_code == 400:
            idx = (idx+1)%len(keys)
            continue
        items = r.json()

        conn = psycopg2.connect(
        database="videos", user='postgres', password='1234', host='localhost', port= '5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        for item in items['items']:
            record = [item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['publishedAt'], item['snippet']['thumbnails']['default']['url']]
            query = '''INSERT INTO public."SearchApp_videos" ("VideoId", "VideoTitle", "VideoDescription", "UploadTime", "ThumbnailURL") VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING'''
            cursor.execute(query, record)
            conn.commit()

        conn.close()

class SearchappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SearchApp'

    def ready(self):
        t = threading.Thread(target=http_call_async)
        t.setDaemon(True)
        t.start()