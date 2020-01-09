from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='YOUR_API_KEY')

news_sources = newsapi.get_sources()
for source in news_sources['sources']:
    print(source['name'])

top_headlines = newsapi.get_top_headlines(
    q='World War',
    language='en',
)
for article in top_headlines['articles']:
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')

all_articles = newsapi.get_everything(
    q='World War',
    language='en',   
)
for article in all_articles['articles']:
    print('Source : ',article['source']['name'])
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')



    