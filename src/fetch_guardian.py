import requests
import csv

API_KEY = "f52152eb-3943-4fd0-a894-508771436000"

url = "https://content.guardianapis.com/search"

params = {
    "api-key": API_KEY,
    "page-size": 100,
    "show-fields": "bodyText"
}

response = requests.get(url, params=params)
data = response.json()

results = data["response"]["results"]

with open("guardian_articles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "title",
        "section",
        "date",
        "url",
        "text"
    ])

    for article in results:
        fields = article.get("fields", {})
        writer.writerow([
            article.get("webTitle"),
            article.get("sectionName"),
            article.get("webPublicationDate"),
            article.get("webUrl"),
            fields.get("bodyText")
        ])

print("Downloaded", len(results), "articles")