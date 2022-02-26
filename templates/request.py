# from newsapi import NewsApiClient
from app import app
import urllib.request,json
from .models import articles
Articles=articles.Articles
Sources=articles.Sources


#Getting api key
api_key=app.config['NEWS_API']

#Getting the news articles base url
base_url=app.config["NEWS_API_BASE_URL"]
base2_url=app.config["NEW_NEWS"]

def get_articles(source):
  '''
  Func that gets the json response to url request
  '''
  get_articles_url=base_url.format(source,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data=url.read()
    get_articles_res=json.loads(get_articles_data)

    article_results = None

    if get_articles_res['articles']:
      article_results_list=get_articles_res['articles']
      article_results=process_results(article_results_list)

  return article_results      



def process_results(articles_list):
  '''
  Processes results and transform them to a list of objects
  Arg:
    articles_list:list of dictionaries that contain movie details
  '''
  article_results=[]
  for article_item in articles_list:
    urlToImage=article_item.get('urlToImage')
    title=article_item.get('title')
    description=article_item.get('description')
    url=article_item.get('url')
    time=article_item.get('publishedAt')
    content=article_item.get('content')


    if urlToImage:
      article_object=Articles(urlToImage,title,description,url,time,content)
      article_results.append(article_object)

  return article_results





def get_source(sources):
  get_source_url=base2_url.format(sources,api_key)
  
  with urllib.request.urlopen(get_source_url) as url:
    get_source_data=url.read()
    get_source_res=json.loads(get_source_data)

    source_results = None
    
    if get_source_res['sources']:
      source_results_list=get_source_res['sources']
      source_results=process_result(source_results_list)

  return source_results     

def process_result(source_list):
  '''
  Processes results and transform them to a list of objects
  Arg:
    articles_list:list of dictionaries that contain movie details
  '''
  source_results=[]
  for source_item in source_list:
    id=source_item.get('id')
    name=source_item.get('name')
    url=source_item.get('url')
    

    if id:
      source_object=Sources(id,name,url)
      source_results.append(source_object)

  return source_results 
