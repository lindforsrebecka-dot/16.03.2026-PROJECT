# Visualisations based on the comparison of LabMT 1.0 and The Guardian Dataset

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def print_section(title: str) -> None:
    bar = "=" * 90
    print("\n" + bar)
    print(title)
    print(bar)


def save_csv(df: pd.DataFrame, filename: str, index: bool = False) -> None:
    out_path = TABLES_DIR / filename
    df.to_csv(out_path, index=index)
    print(f"Saved table: {out_path}")


def save_figure(filename: str, dpi: int = 200) -> None:
    out_path = FIGURES_DIR / filename
    plt.savefig(out_path, dpi=dpi)
    print(f"Saved figure: {out_path}")

# Project paths

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "Data_Set_S1.txt"
WORLD_PATH = ROOT / "data" / "processed" / "world_tokens_matched.csv"
SPORT_PATH = ROOT / "data" / "processed" / "sport_tokens_matched.csv"
CULTURE_PATH = ROOT / "data" / "processed" / "culture_tokens_matched.csv"

FIGURES_DIR = ROOT / "figures"
TABLES_DIR = ROOT / "tables"

FIGURES_DIR.mkdir(exist_ok=True)
TABLES_DIR.mkdir(exist_ok=True)


print_section("1.1 Load the dataset (Data_Set_S1.txt)")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Dataset not found. Expected to find: "
        f"{DATA_PATH}\n\n"
        "Make sure Data_Set_S1.txt is in data/raw/ and try again."
    )


df = pd.read_csv(
    DATA_PATH,
    sep="\t",
    skiprows=3,
    na_values=["--"],
    encoding="utf-8",
)

print(df.shape[0])
print(df.shape[1])


labmt = pd.read_csv(
    DATA_PATH,
    sep="\t",        # tab delimited
    skiprows=3,      
    na_values=["--"],
    encoding="utf-8"
)

numeric_cols = [
    "happiness_rank",
    "happiness_average",
    "happiness_standard_deviation",
    "twitter_rank",
    "google_rank",
    "nyt_rank",
    "lyrics_rank",
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["word"] = df["word"].astype("string")




# 1. Histogram


world = pd.read_csv(WORLD_PATH).dropna(subset=["Happiness Score"])
sport = pd.read_csv(SPORT_PATH).dropna(subset=["Happiness Score"])
culture = pd.read_csv(CULTURE_PATH).dropna(subset=["Happiness Score"])

plt.figure(figsize=(8,5))
plt.hist(labmt["happiness_average"].dropna(), bins=40, alpha=0.4, color="gray", label="labMT")
plt.hist(world["Happiness Score"], bins=40, alpha=0.4, color="blue", label="World")
plt.hist(sport["Happiness Score"], bins=40, alpha=0.4, color="orange", label="Sport")
plt.hist(culture["Happiness Score"], bins=40, alpha=0.2, color="green", label="Culture")
plt.title("Histogram of Happiness Scores")
plt.xlabel("Happiness Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("histogram_comparison_happiness_scores.png")
plt.show()



# 2. Violin Plot


categories = ["labMT", "World", "Sport", "Culture"]
data = [
    labmt["happiness_average"].dropna(),
    world["Happiness Score"].to_numpy(),
    sport["Happiness Score"].to_numpy(),
    culture["Happiness Score"].to_numpy()
]

fig, ax = plt.subplots(figsize=(8,5))
parts = ax.violinplot(data, showmedians=True, showextrema=False)

colors = ["gray", "blue", "orange", "green"]
for pc, color in zip(parts['bodies'], colors):
    pc.set_facecolor(color)
    pc.set_alpha(0.6)

ax.set_title("Violin Plot: Happiness Score Distribution")
ax.set_xlabel("Dataset")
ax.set_ylabel("Happiness Score")
ax.set_xticks(np.arange(1, len(categories)+1))
ax.set_xticklabels(categories)
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("violin_happiness_scores.png")
plt.show()



# 3. Q-Q Plot


world = pd.read_csv("./data/processed/world_tokens_matched.csv").dropna(subset=["Happiness Score"])
sport = pd.read_csv("./data/processed/sport_tokens_matched.csv").dropna(subset=["Happiness Score"])
culture = pd.read_csv("./data/processed/culture_tokens_matched.csv").dropna(subset=["Happiness Score"])
labmt = pd.read_csv("data/raw/Data_Set_S1.txt", sep="\t", skiprows=3, na_values=["--"], engine="python")
labmt["happiness_average"] = pd.to_numeric(labmt["happiness_average"], errors="coerce")

labmt_scores = labmt["happiness_average"].dropna().to_numpy()
world_scores = world["Happiness Score"].to_numpy()
sport_scores = sport["Happiness Score"].to_numpy()
culture_scores = culture["Happiness Score"].to_numpy()

fig, ax = plt.subplots(figsize=(7, 5))
colors = {"World": "blue", "Sport": "orange", "Culture": "green"}

labmt_sorted = np.sort(labmt_scores)
q_ref = np.linspace(0, 1, len(labmt_sorted))
labmt_quantiles = np.quantile(labmt_scores, q_ref)

for label, scores in zip(["World", "Sport", "Culture"], [world_scores, sport_scores, culture_scores]):
    cat_sorted = np.sort(scores)
    cat_quantiles = np.quantile(scores, q_ref)
    ax.plot(labmt_quantiles, cat_quantiles, marker='o', linestyle='none', alpha=0.6, color=colors[label], label=label)

ax.plot([labmt_quantiles.min(), labmt_quantiles.max()],
        [labmt_quantiles.min(), labmt_quantiles.max()],
        color="gray", linestyle="--", label="y = labMT")

ax.set_title("Q–Q Plot: The Guardian vs labMT Happiness")
ax.set_xlabel("labMT Quantiles")
ax.set_ylabel("The Guardian Quantiles")
ax.legend()
ax.grid(True, alpha=0.25)

plt.tight_layout()
plt.savefig("qq_plot_categories_vs_labmt.png")
plt.show()