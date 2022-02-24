import json
from urllib.request import urlopen
import time

'''Get comments'''
# supports s,m,h,d 
time_frame = 'h'
comments = []
for i in range(10):
    before = str(i) + time_frame
    after = str(i + 1) + time_frame
    url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=recipes&after={}&before={}'.format(after, before)
    data = json.load(urlopen(url))['data']
    for comment_info in data:
        comments.append(comment_info['body'])

    # print(data)
    print(len(data))

    time.sleep(3)

print(comments)
