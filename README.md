# YoutubeSearchAPI

### Pre-requisites: 
1. Install python and pip
2. Install modules from **requirements.txt**
3. Install Postgresql 
4. Create a database in Postgresql and enter details in DATABASES = {} in **settings.py**
5. Enter same details in line 32 in **SearchApp/apps.py**
6. Run django server using command - **"python manage.py runserver"**


### Testing Get Videos API:

Send GET request to **127.0.0.1/videos** to get video data in a paginated response sorted in descending order of published datetime.

Additionally edit **'$'** in GET request to **127.0.0.1/videos?limit=$&offset=$** to go through pages.


### Testing Search API:

Send POST request to **127.0.0.1/search data = '?'** editing the **'?'**, to get results with **full or partial match** to the search query.


### Note:

The API automatically cycles through multiple API keys in case of exhausted quota.


The project was not Dockerized because of errors due to psycopg2 and few other modules.
