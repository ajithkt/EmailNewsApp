import requests
from send_email import send_email


url=("https://newsapi.org/v2/everything?q=tesla&from=2025-09-04&sortBy=publishedAt&"
     "apiKey=0a9f8103d7514c88806cb59ae215dc8f")

# Make request
request = requests.get(url)

# Get Dictionary with data
content = request.json()

email_content = ""

# Access the article title and description.
for article in content['articles']:
     email_content = email_content + str(article['title']) + "\n" + str(article['description']) + 2*"\n"
     # email_content = email_content + article['title'] + "\n" + article['description'] + 2*"\n"

email_content = email_content.encode("utf-8")
print(email_content)
send_email(email_content)

