import requests

API_KEY = "0a9f8103d7514c88806cb59ae215dc8f"
url=("https://newsapi.org/v2/everything?q=tesla&from=2025-09-04&sortBy=publishedAt&"
     "apiKey=0a9f8103d7514c88806cb59ae215dc8f")

# Make request
request = requests.get(url)

# Get Dictionary with data
content = request.json()

# Access the article title and description.
for article in content['articles']:
     print(article['title'])
     print(article['description'])