import requests
from wordfrequence import frequentWords
from CRYPTOPRICETRACKER import getCoinData
from cleanfile import frequentWords

    
# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('4ZQnNXcF5awF6ZF7XNesXA', 'kxXvJKHo2UEe6nKgtyOoVLO4NJRGpA')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'dev_oskar',
        'password': 'Supra2004'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'dev/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

def get_reddit_thread(threadname : str):
        # while the token is valid (~2 hours) we just add headers=headers to our requests
        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        res = requests.get(f"https://oauth.reddit.com/r/{threadname}/new",
                        headers=headers)
        # loop through each post retrieved from GET request
        posts = []
        for post in res.json()['data']["children"]:
        # append relevant data to dataframe
                posts.append(post["data"]["selftext"])
        return "\n".join(posts)

def textCount(keywords, text):
        talley = {}
        for i in keywords:
                talley[i] = text.count(i)
        return talley
        
                






