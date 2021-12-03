import requests
import praw
import datetime

reddit = praw.Reddit(
    client_id="xpGCUsn0pjGiSdKJF6yz9Q",
    client_secret="ZzsiohoKTEEdwpW_DyPbdiRTYHBRgA",
    password="abbyb34r",
    user_agent="testscript by u/fakebot3",
    username="cbnyc",
)

ff = reddit.subreddit('fantasyfootball')

def get_posts():
    peaked = get_peaked()
    stream = get_stream()
    tvt = get_tvt()
    consolidated = get_consolidated_waiver()
    news = get_news()
    return(peaked, stream, tvt, consolidated, news)

def get_peaked():
    posts = []
    for i in ff.search('title:Reddit Adjusted Trade AND author:PeakedInHighSkool', sort='new', limit=1):
        post = {
        'title' : i.title,
        'url' : i.url,
        'created' : datetime.datetime.fromtimestamp(i.created),
        'num_comments' : i.num_comments,
        'user' : "PeakedInHighSkool"
        }
        posts.append(post)
    return posts

def get_stream():
    posts = []
    for i in ff.search('title:Stream w/Consciousness AND author:subvertadown', sort='new', limit=1):
        post = {
        'title' : i.title,
        'url' : i.url,
        'created' : datetime.datetime.fromtimestamp(i.created),
        'num_comments' : i.num_comments,
        'user' : "subvertadown"
        }
        posts.append(post)
    return posts

def get_tvt():
    posts = []
    for i in ff.search('title:Trade Value Tuesday AND author:HouseBlackfyre', sort='new', limit=1):
        post = {
        'title' : i.title,
        'url' : i.url,
        'created' : datetime.datetime.fromtimestamp(i.created),
        'num_comments' : i.num_comments,
        'user' : "HouseBlackfyre"
        }
        posts.append(post)
    return posts

def get_consolidated_waiver():
    posts = []
    for i in ff.search('title:Consolidated Week AND author:mcphisto2', sort='new', limit=1):
        post = {
        'title' : i.title,
        'url' : i.url,
        'created' : datetime.datetime.fromtimestamp(i.created),
        'num_comments' : i.num_comments,
        'user' : "mcphisto2"
        }
        posts.append(post)
    print(posts)
    return posts

def get_news():
    response = requests.get("http://127.0.0.1:7777/")
    news = response.json()
    news_list = []
    news_list.append(news["1"])
    news_list.append(news["2"])
    news_list.append(news["3"])
    news_list.append(news["4"])
    news_list.append(news["5"])
    return news_list