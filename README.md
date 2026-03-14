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

_https://open-platform.theguardian.com/_   

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

### Visualising Happiness in Guardian Articles

  This section presents the visualisations used to analyse differences in the happiness scores across three topics. The dataset consists of 900 articles from The Guardian, with 300 of each from the World, Sport, and Culture sections. The happiness scores for eahc word is calculated using the labMT 1.0 lexicon, which matches sentiment value to each word and estimates them into a document level of happiness. 
   
  The main goal of these visualisations is to compare the distributionn, variability and differences in happiness between the three topics and to address these observations. 
    


### Happiness scores distribution  

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_scores_distribution.png)

By examining the distribution of happiness scores across all three sections using a histogram, we can see the frequency of the tokenized words' happiness scores on the y-axis and the coresponding happiness value on the x-axis. This plot shows us that most articles fall between a moderate happiness range (around the 5-6 happiness mark), with variations across sections. 




### Happiness by section  

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_by_section_violin_plot.png)

To compare the three sections, we use a violin plot that shows happiness scores by section. The visualisations helps us see better the distribution, density, and spread of the data, such as how the Sport and Culture sections tend to show higher concentrations of happiness of some higher happiness scores compared with the World articles. 

A boxplot was also created, however, it provides very similar insight as the violin plot. The violin plot is therefore more emphasised in the analysis because it offers additionally the full distribution density. 

We can see how the World section has some articles that are close to the level of happiness of 2, commpared to the other two sections, where are almost none. This shows there is way more "sadness" in the World articles. 


### Happiness over time  

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_over_time.png)


Another visualisation looks into happiness scores over time by using a time index on the x-axis and the happiness score on the y-axis. This plot allows us to look into how happiness changes across the dataset in a chronological order. 

We can see however, that there is no significant change. This tells us that happiness is not influenced over time in the Guardian articles. 


### Bootstrap Distribution of Mean Happiness 

In order to understand uncertainty in the estimated scores of average happiness, we geenrate a bootstrap distribution of the mean happiness for each section. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/bootstrap_distribution.png)


The bootstrap results show that:

- Sport articles have the highest mean happiness score (5.62)
- Culture articles have a very similar mean to Sport, only (5.60)
- World articles have a noticeably lower mean happiness (5.39)

This pattern suggests that Sport and Culture articles tend to use slightly more positive language, comapared to the World news articles. 


### Difference in Mean Happiness

A diffence plot of the mean happiness score further shows the comparison between our three sections. We have chosen a plot that  uses the ± 95% confidence interval for a different perspective. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/difference_plot_mean.png)


The plot confirms the pattern already observed in the bootstrap distribution: Sport and Culture articles having higher average happiness than World articles. 

### Ridgeline Distribution Plot

We also created a ridgeline plot to visualise the distribution of happiness scores for all sections. This plot shows information very similar to the violin plot, but it allows easier comparison of how the distributions change on the happiness scale. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/ridgeline_plot.png)

The ridgeline plot highlights the following patterns:

- World articles mostly use words with happiness scores between 4.5 and 6.5.
- Sport articles also begin around the 4.5 mark, but their dsitrubution extends further upward and reach values close to 7, which shows a higher presence of posiive language
- Culture articles begin around the 4.5 mark as well, then show a slight drop in density around 5.5, and then stay relatively elevated until around 6.5.

This visualisation reinforces the observation that Sport and Culture tend to go further up on the happiness range than World articlles.










