# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crucial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"

url = url[0:5] + ":" + url[5:-4] + "odds"

print(url)