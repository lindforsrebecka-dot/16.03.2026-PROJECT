# Inferring Happiness Dynamics in The Guardian

This project analyzes the emotional tone of articles produced by _The Guardian_ using the labMT 1.0 hedonometer.  

The articles are collected through the Open Platform - The Guardian API.   

Each article is analyzed by using the hedonometer to estimate a happiness score. These scores will allow us to view how emotional tone differs across different sections of the news.    

## Folder layout  

- `src/` - Scripts used for data collection and analysis
- `data/raw/` - raw data gathered from the Guardian Open Platform API
- `data/processed/` - processed dataset for analysis
- `figures/` - PNG plots generated
- `tables/` - CSV tables & summaries

## Dataset  

The dataset comes from the Guardian Open Platform (Content API)    

https://open-platform.theguardian.com/   

The API provides access to Guardian's articles and following metadata.  

The following fields are collected:  

- webTitle (article title)
- sectionName (news section)
- webPublicationDate (publication date)
- webUrl (link to article)
- bodyText (article text)

Raw data is stored in:
  -> `data/raw/guardian_articles.csv`  

## How to run the script  

Run the following command:     

`python3 src/fetch_guardian.py`


## Method  

In this second project, our group uses the _labMT 1.0 hedonometer_ to measure the emotional tone of The Guardian articles.  


## Results

### Happiness scores distribution  

(add Figure here) 


### Happiness by section  

(add Figure here)  


### Happiness over time  

(add figure here)  

