# 16.03.2026-PROJECT
Coding assignment

# Guardian News Sentiment Dataset

## Data source
The data comes from the Guardian Open Platform (Content API).

https://open-platform.theguardian.com/

## What this script does
The script `src/fetch_guardian.py` downloads 100 Guardian news articles using the Guardian API.

The following fields are collected:
- webTitle (article title)
- sectionName (news section)
- webPublicationDate (publication date)
- webUrl (link to article)
- bodyText (article text)

## Data location
Raw data is stored in:

data/raw/guardian_articles.csv

## How to run the script

Run the following command:

python3 src/fetch_guardian.py