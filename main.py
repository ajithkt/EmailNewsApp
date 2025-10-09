import requests
from send_email import send_email

topic = "tesla"

API_KEY = "0a9f8103d7514c88806cb59ae215dc8f"
url=("https://newsapi.org/v2/everything?"
     f"q={topic}&"
     "from=2025-09-09&"
     "sortBy=publishedAt&apiKey=0a9f8103d7514c88806cb59ae215dc8f&"
     "language=en")

# Make request
request = requests.get(url)

# Get Dictionary with data
content = request.json()

print(content)
email_content = ""

# Access the article title and description.
for article in content['articles'][:20]:
     email_content = ( email_content + str(article['title']) + "\n" +
                      str(article['description']) + "\n" + article["url"]+ 2*"\n")
     # email_content = email_content + article['title'] + "\n" + article['description'] + 2*"\n"

email_content = "Subject: Today's News" + "\n" + email_content
email_content = email_content.encode("utf-8")
print(email_content)
send_email(email_content)

