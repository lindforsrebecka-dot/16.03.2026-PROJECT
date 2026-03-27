# Visualisations for The Guardian Dataset

# 1. Happiness scores distribution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

categories = {"World": world, "Sport": sport, "Culture": culture}
colors = {"World": "blue", "Sport": "orange", "Culture": "green"}

fig, ax = plt.subplots(figsize=(8,5))
for label, df_cat in categories.items():
    ax.hist(df_cat["Happiness Score"], bins=30, alpha=0.5, label=label, color=colors[label])

ax.set_title("Happiness Scores Distribution by Category")
ax.set_xlabel("Happiness Score")
ax.set_ylabel("Frequency")
ax.legend()
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig("happiness_scores_distribution.png")
plt.show()


# 2. Happiness by section (using Violin Plot)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

categories = {"World": world, "Sport": sport, "Culture": culture}
colors = {"World": "blue", "Sport": "orange", "Culture": "green"}

fig, ax = plt.subplots(figsize=(8,5))
data = [df_cat["Happiness Score"].to_numpy() for df_cat in categories.values()]
parts = ax.violinplot(data, showmedians=True, showextrema=False)
for pc, color in zip(parts['bodies'], colors.values()):
    pc.set_facecolor(color)
    pc.set_alpha(0.6)

ax.set_title("Happiness by Section (Category)")
ax.set_xlabel("Category")
ax.set_ylabel("Happiness Score")
ax.set_xticks(np.arange(1, len(categories)+1))
ax.set_xticklabels(categories.keys())
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("happiness_by_section.png")
plt.show()


# 3. Happiness over time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

categories = {"World": world, "Sport": sport, "Culture": culture}
colors = {"World": "blue", "Sport": "orange", "Culture": "green"}

fig, ax = plt.subplots(figsize=(8,5))
for label, df_cat in categories.items():
    if "date" in df_cat.columns: 
        yearly_avg = df_cat.groupby("date")["Happiness Score"].mean()
        ax.plot(yearly_avg.index, yearly_avg.values, marker='o', label=label, color=colors[label])
    else:
        cumulative_avg = df_cat["Happiness Score"].expanding().mean()
        ax.plot(cumulative_avg, label=label, color=colors[label])

ax.set_title("Happiness Over Time")
ax.set_xlabel("Time / Index")
ax.set_ylabel("Average Happiness Score")
ax.legend()
ax.grid(True, alpha=0.5)
plt.tight_layout()
plt.savefig("happiness_over_time.png")
plt.show()


# 4. Bootstrap distribution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world = pd.read_csv("./data/processed/world_tokens_matched.csv")
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv")
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv")

world["topic"] = "world"
sport["topic"] = "sport"
culture["topic"] = "culture"

df = pd.concat([world, sport, culture], ignore_index=True)
df.groupby("topic")["Happiness Score"].mean()

def bootstrap_mean(data, n_boot=20000):
    means = []
    for _ in range(n_boot):
        sample = np.random.choice(data, size=len(data), replace=True)
        means.append(sample.mean())
    return np.array(means)

world_boot = bootstrap_mean(world["Happiness Score"].dropna())
sport_boot = bootstrap_mean(sport["Happiness Score"].dropna())
culture_boot = bootstrap_mean(culture["Happiness Score"].dropna())

plt.hist(world_boot, bins=40, alpha=0.5, label="World")
plt.hist(sport_boot, bins=40, alpha=0.5, label="Sport")
plt.hist(culture_boot, bins=40, alpha=0.5, label="Culture")

plt.legend()
plt.title("Bootstrap Distribution of Mean Happiness Scores")
plt.xlabel("Mean Score")
plt.ylabel("Frequency")

plt.savefig("bootstrap_distribution.png")
plt.print()


# 5. Strip / Jitter Plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

world = pd.read_csv("./data/processed/world_tokens_matched.csv")
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv")
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv")

world["topic"] = "world"
sport["topic"] = "sport"
culture["topic"] = "culture"

df = pd.concat([world, sport, culture], ignore_index=True)
df = df.dropna(subset=["Happiness Score"])

topics = ["world", "sport", "culture"]
pos = {t: i for i, t in enumerate(topics)}

np.random.seed(0)

x_base = df["topic"].map(pos).astype(float)
x_jit = x_base + (np.random.rand(len(x_base)) - 0.5) * 0.25

fig, ax = plt.subplots(figsize=(8,5))

ax.scatter(x_jit, df["Happiness Score"], s=10, alpha=0.5)

ax.set_xticks(range(len(topics)))
ax.set_xticklabels(topics)
ax.set_xlabel("Topic")
ax.set_ylabel("Happiness Score")
ax.set_title("Strip / Jitter plot of token happiness scores by topic")

ax.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("strip_plot.png")
plt.show()


# 6. Ridgeline Plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

df = pd.concat([world, sport, culture], ignore_index=True)
df = df.dropna(subset=["Happiness Score"])

topics = ["world", "sport", "culture"]

x_grid = np.linspace(df["Happiness Score"].min(),
                     df["Happiness Score"].max(), 300)

fig, ax = plt.subplots(figsize=(8,5))

for i, topic in enumerate(topics):

    vals = df.loc[df["topic"] == topic, "Happiness Score"].values

    if len(vals) < 5:
        continue

    kde = gaussian_kde(vals)
    dens = kde(x_grid)
    dens = dens / dens.max()

    ax.fill_between(x_grid, i, i + dens * 0.8, alpha=0.7)
    ax.plot(x_grid, i + dens * 0.8)

ax.set_title("Ridgeline plot of happiness scores by topic")
ax.set_xlabel("Happiness Score")
ax.set_yticks([i + 0.4 for i in range(len(topics))])
ax.set_yticklabels(topics)

ax.grid(True, axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig("ridgeline_plot.png")
plt.show()


# 7. Violin Plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyreadstat  

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

categories = ["World", "Sport", "Culture"]
data = [
    world["Happiness Score"].to_numpy(),
    sport["Happiness Score"].to_numpy(),
    culture["Happiness Score"].to_numpy()
]

fig, ax = plt.subplots(figsize=(8,5))
parts = ax.violinplot(data, showmedians=True, showextrema=False)

colors = ["blue", "orange", "green"]
for pc, color in zip(parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_alpha(0.6)

ax.set_title("Violin Plot: Happiness Score Distribution by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Happiness Score")
ax.set_xticks(np.arange(1, len(categories) + 1))
ax.set_xticklabels(categories)

ax.grid(True, axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig("violin_plot2.png")
plt.show()


# 8. Boxplot

sns.boxplot(x="topic", y="Happiness Score", data=df, palette=["blue", "orange", "green"])
sns.stripplot(x="topic", y="Happiness Score", data=df, color="black", size=2, jitter=True)
plt.savefig("boxplot.png")
plt.show()


# 9. Difference plot (Mean ± 95% CI)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

def bootstrap_mean(data, n_boot=20000):
    means = []
    for _ in range(n_boot):
        sample = np.random.choice(data, size=len(data), replace=True)
        means.append(sample.mean())
    return np.array(means)

world_boot = bootstrap_mean(world["Happiness Score"])
sport_boot = bootstrap_mean(sport["Happiness Score"])
culture_boot = bootstrap_mean(culture["Happiness Score"])

def mean_ci(boot):
    mean = boot.mean()
    ci = np.percentile(boot, [2.5, 97.5])
    return mean, ci

world_mean, world_ci = mean_ci(world_boot)
sport_mean, sport_ci = mean_ci(sport_boot)
culture_mean, culture_ci = mean_ci(culture_boot)

categories = ["World", "Sport", "Culture"]
means = [world_mean, sport_mean, culture_mean]
cis = [world_ci, sport_ci, culture_ci]
colors = ["blue", "orange", "green"]

fig, ax = plt.subplots(figsize=(8,5))

for i, (mean, ci, color) in enumerate(zip(means, cis, colors)):
    ax.errorbar(i+1, mean, yerr=[[mean - ci[0]], [ci[1] - mean]],
                fmt='o', color=color, capsize=6, markersize=8, label=categories[i])

ax.set_xticks(np.arange(1, len(categories)+1))
ax.set_xticklabels(categories)
ax.set_ylabel("Mean Happiness Score")
ax.set_title("Mean Happiness Score ± 95% Confidence Interval by Category")
ax.grid(True, axis="y", alpha=0.25)
ax.legend()

plt.tight_layout()
plt.savefig("difference_plot_mean.png")
plt.show()


# 10. Top contributing words bar chart

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])

categories = {"World": world, "Sport": sport, "Culture": culture}
colors = {"World": "blue", "Sport": "orange", "Culture": "green"}

fig, axs = plt.subplots(3, 1, figsize=(10,12))

for i, (label, df_cat) in enumerate(categories.items()):
    token_avg = df_cat.groupby("token")["Happiness Score"].mean()
    
    top_pos = token_avg.nlargest(10)
    top_neg = token_avg.nsmallest(10)
    top_tokens = pd.concat([top_neg, top_pos])
    
    axs[i].bar(top_tokens.index, top_tokens.values, color=colors[label])
    axs[i].set_title(f"Top contributing words: {label}")
    axs[i].set_ylabel("Average Happiness Score")
    axs[i].tick_params(axis="x", rotation=45)
    
plt.tight_layout()
plt.savefig("top_contributing_words_bar_chart.png")
plt.show()
