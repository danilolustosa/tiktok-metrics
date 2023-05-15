import requests
from bs4 import BeautifulSoup
import os
import slate3k
import re
from post import Post

def log(filename, content):
    with open(filename + '.txt', 'w') as f:
        f.write(content)

url = "https://www.tiktok.com/@" + "danlustosaoficial"
response = requests.get(url, headers={})
html_string = response.text
soup = BeautifulSoup(html_string, "html.parser")   
body = soup.find_all('body')   
div_posts = body[0].find_all("div", "tiktok-x6y88p-DivItemContainerV2 e19c29qe7")

posts = []

for div_post in div_posts:
    label = div_post.find("div", "tiktok-5lnynx-DivTagCardDesc eih2qak1")
    views = div_post.find("strong", "video-count tiktok-1nb981f-StrongVideoCount e148ts222")
    url_post = div_post.find("a", href=True)['href']

    posts.append(
        {
            "id": url_post.split('/')[5],
            "label": label.text,
            "views": int(views.text),
            "url": url_post,
            "likes": 0
        }
    )

post = Post()
post.read(posts)

# for post in posts:
#     print(post["url"])

#     response = requests.get(post["url"], headers={})
#     soup = BeautifulSoup(html_string, "html.parser")   
#     body = soup.find_all('body')

    
#     log(post["id"], str(body))


#     # span_title = body[0].find("span", {"data-e2e": "browser-nickname"})
#     # print("Title: ", span_title )

#     span_likes = body[0].find("strong",{"title": "Followers"})
#     print(span_likes.text)
#     #post["likes"] = int(span_likes.text)


#     print("-----------------")

    
