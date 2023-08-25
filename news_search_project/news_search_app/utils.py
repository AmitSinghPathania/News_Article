import requests

def fetch_articles(keyword):
    api_key = "YOUR_API_KEY"
    url = f"https://newsapi.org/v2/everything?q={keyword}&from=2023-07-24&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    return articles
