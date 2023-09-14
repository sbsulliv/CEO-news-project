import requests

API_KEY = '83b637f89d7e4bddac643c0cd1d6d9c7'

KEYWORDS = ' OR '.join(['bankruptcy', 'bankrupt', 'insolvency', 'insolvent', 'merger', 'acquisition'])

endpoint = 'https://newsapi.org/v2/everything'
params = {
    'apiKey': API_KEY,
    'q': KEYWORDS,
    'sortBy': 'publishedAt', 
    'language': 'en', 
}

response = requests.get(endpoint, params=params)

if response.status_code == 200:
    data = response.json()
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}\n")
else:
    print(f"Failed to retrieve news articles. HTTP Status code: {response.status_code}")
