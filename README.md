# Inferring Happiness Dynamics in The Guardian

This project analyzes the emotional tone of articles produced by _The Guardian_ using the **labMT 1.0 hedonometer**.  

By analyzing articles collected from the **Guardian Open Platform API**, this project aims to estimate happiness scores based on the values assigned to each words in the **labMT** data.  

Main aim of this project is to compare how emotional tone differs in each news sections and examine differences in language used in different journalistic aspects.  


## Folder layout  

- `src/` - Scripts used for data collection and analysis
- `data/raw/` - raw data gathered from the Guardian Open Platform API
- `data/processed/` - processed dataset for analysis
- `figures/` - PNG plots generated
- `tables/` - CSV tables & summaries

## Method
In our project, we are analysing the emotional tone of **900 articles by The Guardian** by using a **labMT 1.0 hedonometer**. It is a lexicon-based sentiment analysis tool that assigns happiness scores to individual words. We are combining article collection and lexical sentiment scoring to compare emotional tones across sections. 

For our data collection, we are using the **Guardian Open Platform Content API**, which provides access to full article texts from The Guardian. For our data, we are concentrating on three main sections, `World`, `Sport` and `Culture` with a Python script. Each section consists of **300 articles**.   

These articles were extracted by various fields: 

`webTitle` – article title  
`sectionName` – Guardian news section  
`webPublicationDate` – publication date  
`webUrl` – article link  
`bodyText` – full article text  


The raw dataset was saved as:
`data/raw/guardian_articles.csv`  

#### _Text preprocessing_

Our preprocessing pipeline of the articles consisted of three main parts

1. **Tokenization** - splitting article text into individual word tokens
2. **Normalization** - converting the tokens to lowercase to ensure consistency and matching with the sentiment lexicon.
3. **Filtering** - removing punctuation.

#### _Scoring_
   
We matched the cleaned tokens with the **labMT hedonometer**, which contains English words rated on a happiness scale from **1 (least happy) to 9 (most happy)**.   

Each of the 900 articles' emotional tone was estimated with the hedonomenter and matched with their corresponding labMT happiness scores. To receive an **average happiness score**, we took the mean of the happiness value of all matched tokens. This way we were able to produce a document level happiness score, which reveals the emotional tone of the article.     

#### _Statistical Analysis and Visualisation_

To find differences in emotional tones across our sections, we applied visualization and statistical techniques to our project. We used various visualisation and statistical techniques: 

- **Histogram** distributions to show frequency of happiness values,
- **Violin plots** to compared distribution shape and densities,
- **Time-series visualisation** to explore differences over publication dates,
- **Bootstrap resampling** to estimate uncertainty in mean happinesss scores,
- **Confidence interval comparisons** to evaluate differences between section means,
- **Word contribution analysis** to identify words with the largest impact on happiness scores. 

#### _Comparison with labMT Dataset_

The distribution of happiness scores in the dataset between the Guardian and the original **labMT lexicon** distribution were compared by using _histograms_ and _violin plots_. This comparison helps contextualize how the emotional tone of Guardian articles relates to the baseline sentiment distribution of the lexicon.

All scripts used for this project and data collection are located in the `src/` directory. Our project is designed to run within a Python virtual environment. Running the script `src/fetch_guardian.py` reproduces the article collection process through the used Guardian API. 


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

---

## Results

### Visualising Happiness in Guardian Articles

  - This section presents the visualisations used to analyse differences in the happiness scores across three sections of *The Guardian*: **World**, **Sport**, **Culture**.  
  - The dataset consists of **900 articles**, each section consisted **300 articles**.  
  - Happiness scores are measured using the **labMT 1.0 lexicon, which matches sentiment value to each word and estimates them into a document level of happiness. 
  - The main goal of these visualisations is to compare the _distribution_, _variability_ and _differences in happiness_ between the three topics and to address these observations. 
    


### Happiness scores distribution  


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_scores_distribution.png)
<p align="center"><sub><em>Figure 1. Distribution of happiness scores across World, Sport, and Culture sections. </em></sub>


By examining the distribution of happiness scores across all three sections using a histogram, we can analyze how frequently different happiness values appear.  

The x-axis represents the happiness value, and the y-axis represents the frequency of words with corresponding values.  

The histogram indicates that most values fall bewteen **5-6** happiness range, with variations across sections. 


### Happiness by section  


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_by_section_violin_plot.png)  
<p align="center"><sub><em>Figure 2. Violin plot showing distribution of happiness scores across World, Sport, and Culture sections. </em></sub></p>

To compare the three sections, we used a **violin plot** that shows happiness scores by section. The violin plot helps us to better visualize the distribution, density, and spread of the data.  

The plot indicates that **Sport** and **Culture** articles tend to have slightly higher concentrations of higher happiness scores compared to the **World** articles. 

A **boxplot** was also created, however, it provides very similar insight as the violin plot. The violin plot is therefore more emphasised in the analysis because it offers additionally the full distribution density. 

We can see how the **World** section has some articles that are close to the level of happiness of **2**, compared to the other two sections, where are almost none. This shows there is way more **"sadness"** in the World articles. 


### Happiness over time  


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/5c8f39037aa8274f8d9c8fd1130a88cc5b31b109/figures/happiness_over_time.png)
<p align="center"><sub><em>Figure 3. Average happiness scores over time for World, Sport, Culture sections.</em></sub>

Another visualisation looks into **happiness scores over time** by using a time index on the x-axis and the happiness score on the y-axis.   

This plot allows us to look into how happiness changes across the dataset in a chronological order. 

We can see however, that there is no significant change. This indicates that there is **no significant temporal shifts** in happinness across each articles. 


### Bootstrap Distribution of Mean Happiness Scores

In order to understand uncertainty in the estimated scores of average happiness, we generated a **bootstrap distribution of the mean happiness** for each section. 

<p align="center">
    <img src="https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/bootstrap_distribution.png" width="700">
      </p>
<p align="center"><sub><em>Figure 4. Bootstrap distribution of Mean Happiness scores across World, Sport, and culture sections.</em></sub>

The bootstrap results visualizes that 

- **Sport** articles have the highest mean happiness score (**5.62**)
- **Culture** articles have a very similar mean to Sport, only (**5.60**)
- **World** articles have a noticeably lower mean happiness (**5.39**)

This pattern suggests that **Sport** and **Culture** articles tend to use slightly more positive language, comapared to the **World** news articles. 


### Difference in Mean Happiness

This plot compares the mean happiness scores between three sections using ±95% confidence intervals. This provides an additional aspect of how differences emerge between World, Sport, and Culture articles. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/difference_plot_mean.png)
<p align="center"><sub><em>Figure 5. Comparison of Mean Happiness Scores in World, Sport, and Culture articles.</em></sub>


The plot confirms the pattern already observed in the bootstrap distribution: Sport and Culture articles having higher average happiness than World articles. 


### Ridgeline Distribution Plot

We also created a ridgeline plot to visualise the distribution of happiness scores for all sections. This plot shows information very similar to the violin plot, but it allows for easier comparison of how the distributions change on the happiness scale. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/1912ccf84fb4ae90c62266ce4d2c0e2e36475621/figures/ridgeline_plot.png)
<p align="center"><sub><em>Figure 6. Ridgeline distribution of happiness scores across World, Sport, and Culture articles.</em></sub>

The ridgeline plot highlights the following patterns:

- World articles mostly use words with happiness scores between **4.5** and **6.5**.
- Sport articles also begin around the **4.5** mark, but their distriubution extends further upward and reach values close to **7**, which indicates a higher presence of positive language
- Culture articles begin around the **4.5** mark as well, then show a slight drop in density around **5.5**, and then stay relatively elevated until around **6.5**.

This visualisation reinforces the observation that Sport and Culture tend to reach higher values on the happiness range than World articles. It also shows that World articles have a slight dent around the value of **2** for happiness scores.


### Top Contributing Words

We use a bar chart of the top contributing words to identify the words contributing the most in each section. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/top_contributing_words_bar_chart.png)
<p align="center"><sub><em>Figure 7. Top contributing words to happiness scores in World, Sport, and Culture sections based on labMT lexicon.</em></sub>

From this chart, various observations were made: 

- In the **World** section, the word `Mexico` apprears among the happiest contributing words, which shows Guardian's tendency around specific international news.
- In the **Sport** section, the word `rock` appears as a highly positive word, though usually it is used metaphorically instead of literally.
- In the Culture section, the word "Christmas" also is a highly positive word.

The analysis also shows some interesting nuances. For example, the word `cry` appears in the Culture section with a relatively low happiness score (around **3**), even though in some contexts `crying` might happen in a positive or situations that are emotionally moving. 

Another interesting observation among all section is the word `free`, which consistently appears as one of the words with the highest happiness scores. However, its meaning can vary a significant amount depending on context, which shows how sentiment dictionaries might assign higher scores to words even when their usage differs. 

---

## Comparison with the labMT Dataset

In order to understand better the happiness distribution of Guardian articles and how it compares with the lexicon, we also analyse the **labMT dataset** used in our first assignment. 


### Histogram Comparison


We start by configuring a histogram comparison that shows the happiness score distribution of the three Guardian topics, alongside the labMT dataset.

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/histogram_comparison_happiness_score.png)
<p align="center"><sub><em>Figure 8. Histogram comparison of happiness scores distribution</em></sub>

We can see how the **labMT dataset shows a much higher frequency** of the words overall and a greater number of words that have high happiness scores. In contrast, the Guardian articles have fewer words and show a **narrower distribution** in the histogram.


### Q-Q Plot Comparison

A Q-Q plot was created to compare the happiness score distributions of the three topics with the labMT dataset. 

![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/qq_plot_categories_vs_labmt.png)
<p align="center"><sub><em>Figure 9. Q-Q plot comparing happiness score distribution of each sections with labMT dataset.</em></sub>

In this plot:

- the **labMT dataset** follows the _y = x_ line, which represents a perfect match between both the theoretical and observed distributions.
- the **Sport** and **Culture** distributions are generally above this line, showing relatively higher happiness scores compared with the labMT baseline.
- the **World** distribution falls below the line at the lower happiness values (around **2**-**3**), which suggests that this section contains more negative words than it would be expected based on the general distribution of the lexicon.


### Violin Plot Comparison


![](https://github.com/lindforsrebecka-dot/16.03.2026-PROJECT/blob/ba506d5d18a09ccf1c361dae5a81d488a9090d32/figures/violin_happiness_scores.png)
<p align="center"><sub><em>Figure 10. Violin plot comparing the distribution of happiness scores of the Guardian articles and labMT dataset.</em></sub></p>

In this violin plot we can see that the overall shapes of the distributions are similar to each other. However, the Guardian article distribution seem narrower. This suggests that the articles use a specific subset of language, instead of the full range of words used in the **labMT lexicon**.

## Summary of our Visual Findings

There are a few consistent patterns across all visualisations:

- **Sport articles** show the highest average happiness scores
- **Culture articles** have a similar but slightly lower happiness value than Sport articles
- **World articles** tend to have more negatively scored words

Even though the differences are **not extreme**, they appear consistently across multiple visualisations, including bootstrap distributions, difference plots, and happiness analysis of tokenized words.  


## Credits  

- _Repo & Workflow lead_ - Garam Jeong
- _Data acquisition lead_ - Shenru Wang
- _Measurement lead_ - Rebecka Lindfors
- _Stats & sampling lead_ - Gabriella Cohen
- _Visualisation lead_ - Selin Tefic

## Discussion

This analysis shows how computational text analysis can be used to explore emotional patterns in journalistic writing. By applying the **labMT hedonometer** to a collection of _the Guardian_ articles, we were able to compare how emotional tone varies across 3 different news sections: `World`, `Sport`, and `Culture`.  

For researchers in the **digital humanities** or **media studies**, this approach provides a way to examine large collections of news articles and identify patterns in language use that may not be visible through close reading alone.  

There are several **limitations** to this analysis,  

**First, the sentiment scores rely on the `labMT lexicon`**, meaning that only words included in the lexicon can be assigned a happiness score. Words that are not present in the lexicon cannot be included in the sentiment calculation.  

**Second, lexicon-based sentiment analysis does not account for context**. Words receive fixed happiness values regardless of how they are used. For example, a word such as cry may appear in negative contexts but can also express strong positive emotions. These differences cannot be captured by the method.  

**Finally, the **size of the dataset** may also limit the analysis**. Although the dataset includes **900 articles**, analysing a larger dataset or a longer time period could potentially reveal additional patterns.

## Conclusion
This project analysed the emotional tone of 900 Guardian articles using the labMT 1.0 hedonometer. Sport and Culture articles tend to have slightly higher happiness scores, while World articles show lower values.
Overall, the project demonstrates how computational sentiment analysis can help explore patterns in journalistic language while also highlighting the importance of interpreting lexicon-based results carefully.
 
## Citations  

- Dodds, Peter Sheridan, Kameron Decker Harris, Isable M. Kloumann, Catherine A. Bliss, and Christopher M. Danforth. 2011. "Temporal Patterns of Happiness and Information in a Global Social Netowrk: Hedonometrics and Twitter." _PLoS ONE_ 6 (12): e26752. https://doi.org/10.1371/journal.pone.0026752  

- The Guardian Open Platform API
  : https://open-platform.theguardian.com

- Dataset
  : labMT 1.0 dataset ("Language Assessment by Mechanical Turk") 




