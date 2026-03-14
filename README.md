# Inferring Happiness Dynamics in The Guardian

This project analyzes the emotional tone of articles produced by _The Guardian_ using the **labMT 1.0 hedonometer**.  

By analyzing articles collected from the **Guardian Open Platform API**, this project aims to estimate happiness scores based on the values assigned to each words in the **labMT** data.  

Main aim of this project is to compare how emotional tone differs in each news sections and examine differences in languaged used in different journalistic aspects.  


## Folder layout  

- `src/` - Scripts used for data collection and analysis
- `data/raw/` - raw data gathered from the Guardian Open Platform API
- `data/processed/` - processed dataset for analysis
- `figures/` - PNG plots generated
- `tables/` - CSV tables & summaries

## Dataset  

The dataset comes from the **Guardian Open Platform (Content API)**.   

_https://open-platform.theguardian.com/_   

Total number of **900 articles** were gathered, each from:  

- **300 articles from World**
- **300 articles from Sport**
- **300 articles from Culture**

The API grants access to publications of The Guardian with associated metadata.  

For each articles, the following fields are collected:  

- `webTitle` (article title)
- `sectionName` (news section)
- `webPublicationDate` (publication date)
- `webUrl` (link to article)
- `bodyText` (article text)

And the raw data is stored in:  

`data/raw/guardian_articles.csv`   


## Setup + Run   

#### 1) _Create a virtual environment_  

**macOS / Linux**  
```bash
python3 -m venv .venv
source .venv/bin/activate 
python3 -m pip install --upgrade pip
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
./.venv/Scripts/Activate.ps1
py -m pip install --upgrade pip
```

#### 2) _Install dependencies_  
```bash
python3 -m pip install -r requirements.txt
```

#### 3) _Fetch articles_
```bash
python3 src/fetch_guardian.py
```

## Method  

In this second project, our group uses the _labMT 1.0 hedonometer_ to measure the emotional tone of The Guardian articles.  


## Results

### Visualising Happiness in Guardian Articles

  - This section presents the visualisations used to analyse differences in the happiness scores across three sections of *The Guardian*: **World**, **Sport**, **Culture**.  
  - The dataset consists of **900 articles**, each section consisted **300 articles**.  
  - Happiness scores are measured using the **labMT 1.0 lexicon, which matches sentiment value to each word and estimates them into a document level of happiness. 
  - The main goal of these visualisations is to compare the _distribution_, _variability_ and _differences in happiness_ between the three topics and to address these observations. 
    


### Happiness scores distribution  


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_scores_distribution.png)
<p align="center"><sub><em>Figure 1. Distribution of happiness scores across World, Sport, and Culture sections </em></sub>


By examining the distribution of happiness scores across all three sections using a histogram, we can analyze how frequently different happiness values appear.  

The x-axis represents the happiness value, and the y-axis represents the frequency of words with corresponding values.  

The histogram indicates that most values fall bewteen **5-6** happiness range, with varations across sections. 


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

This visualisation reinforces the observation that Sport and Culture tend to go further up on the happiness range than World articlles and that World articles have a slight dent around the 2 value for happiness scores.


### Top Contributing Words

We use a bar chart of the top contributing words to identify the words that influence happinesss the most in each section. There are various observations that we see:

- In the World section, the word "Mexico" apprears among the happiest contributing words, which shows Guardian's tendency around specific international news.
- In the Sport section, the word "rock" appears as a highly positive word, though usually iy is used metaphorically instead of literally.
- In the Culture section, the word "Christmas" also is a highly positive word.

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/top_contributing_words_bar_chart.png)


The analysis also shows some interesting nuances. For example, the word "cry" appears in the Culture section with a relatively low happiness score (around 3), even though in some contexts crying might happen in a positive or situations that are emotionally moving. 

Another interesting observation among all section is the word "free", which consistently appears as one of the words with the highest happiness scores. However, its meaning can very a significant amount depending on context, which shows how sentiment dictionaries might assign higher scores to words even when their usage differs. 


### Comparison with the labMT Dataset

In order to understand better the happiness distribution of Guardian articles and how it compares with the lexicon, we also analyse the labMT dataset used in our first assignment. 


#### Histogram Comparison


We start by configuring a histogram comparison that shows the happiness score distribution of the three Guardian topics, alongside the labMT dataset.

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/histogram_comparison_happiness_score.png)

We can see how the labMT dataset shows a much higher frequency of the words overall and a greater number of words that have high happiness scores. In contrast, the Guardian articles have fewer words and show a narrower distribution in the histogram.


#### Q-Q Plot Comparison

Using a Q-Q plot we can compare the happiness scoe distributions of the three topics with the labMT dataset. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/qq_plot_categories_vs_labmt.png)

In this plot:

- the labMT dataset follows the y = x line, which represent a perfect match between both the theoretical and observed distributions.
- the Sport and Culture distributions are generally above this line, showing relatively higher happiness scores compared with the labMT baseline.
- the World distribution falls below the line at the lower happiness values (around 2-3), which suggests that this section contains more negative words than it would be expected bsed on the general distribution of the lexicon.


#### Violin Plot Comparison


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/violin_happiness_scores.png)


In the violin plot we can see that the overall shapes of the distributions are similar to each other. However, the Guardian article distribution seem narrower, showing that they use a specific subset of language, instead of the full range of words used in the labMT lexicon.

### Summary of our Visual Findings

There are a few consistent patterns across all visualisations:

- Sport articles show the highest average happiness scores
- Culture articles have a similar but slightly lower happiness value than Sport articles
- World articles tend to have more negatively scored words

Even though the differences are not that extreme, they appear consistently acorss multiple visualisations, including bootstrap distributions, difference plots, and happiness analysis of tokenized words.
 








