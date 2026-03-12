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

def ci(data):
    return np.percentile(data, [2.5, 97.5])

print("World CI:", ci(world_boot))
print("Sport CI:", ci(sport_boot))
print("Culture CI:", ci(culture_boot))

diff = sport_boot - world_boot

difference = np.percentile(diff, [2.5, 97.5])
print("difference between sport and world", difference)
diff = sport_boot - culture_boot

difference = np.percentile(diff, [2.5, 97.5])
print("difference between sport and culture", difference)

diff = culture_boot - world_boot

difference = np.percentile(diff, [2.5, 97.5])
print("difference between culture and world", difference)

#This visually shows the bootstrap distribution

plt.hist(world_boot, bins=40, alpha=0.5, label="World")
plt.hist(sport_boot, bins=40, alpha=0.5, label="Sport")
plt.hist(culture_boot, bins=40, alpha=0.5, label="Culture")

plt.legend()
plt.title("Bootstrap Distribution of Mean Happiness Scores")
plt.xlabel("Mean Score")
plt.ylabel("Frequency")

plt.show()

# interval plot (Seaborn is made for statistics so it is easier to use when producing an interval plot)

sns.pointplot(data=df, x="topic", y="Happiness Score", errorbar=("ci",95))
plt.title("Interval plot of the means")
plt.show()