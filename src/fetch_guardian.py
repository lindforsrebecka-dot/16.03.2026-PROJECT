import requests
import csv

API_KEY = "f52152eb-3943-4fd0-a894-508771436000"

url = "https://content.guardianapis.com/search"
sections = ["world", "sport", "culture"]

with open("guardian_articles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "title",
        "section",
        "date",
        "url",
        "text"
    ])

    for section in sections:
        collected = 0
        page = 1

        while collected < 300:
            params = {
                "api-key": API_KEY,
                "section": section,
                "page-size": 200,
                "page": page,
                "show-fields": "bodyText"
            }

            response = requests.get(url, params=params)
            data = response.json()
            results = data["response"]["results"]

            for article in results:
                if collected >= 300:
                    break

                fields = article.get("fields", {})
                writer.writerow([
                    article.get("webTitle"),
                    article.get("sectionName"),
                    article.get("webPublicationDate"),
                    article.get("webUrl"),
                    fields.get("bodyText")
                ])

                collected += 1

            page += 1

        print("Downloaded", collected, "articles from", section)