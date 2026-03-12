import pandas as pd

# load tokens
world_tokens = pd.read_csv("data/processed/world_tokens.csv")
sport_tokens = pd.read_csv("data/processed/sport_tokens.csv")
culture_tokens = pd.read_csv("data/processed/culture_tokens.csv")

# load labMT
labmt = pd.read_csv("data/raw/Hedonometer.csv")

# lowercase
world_tokens["token"] = world_tokens["token"].str.lower()
sport_tokens["token"] = sport_tokens["token"].str.lower()
culture_tokens["token"] = culture_tokens["token"].str.lower()

labmt["Word"] = labmt["Word"].str.lower()

# keep only needed columns from labMT
labmt_small = labmt[["Word", "Happiness Score"]]

# merge
world = world_tokens.merge(labmt_small, left_on="token", right_on="Word", how="left")
sport = sport_tokens.merge(labmt_small, left_on="token", right_on="Word", how="left")
culture = culture_tokens.merge(labmt_small, left_on="token", right_on="Word", how="left")

# keep only token + score
world = world[["token", "Happiness Score"]]
sport = sport[["token", "Happiness Score"]]
culture = culture[["token", "Happiness Score"]]

# save
world.to_csv("data/processed/world_tokens_matched.csv", index=False)
sport.to_csv("data/processed/sport_tokens_matched.csv", index=False)
culture.to_csv("data/processed/culture_tokens_matched.csv", index=False)

print("Saved matched files.")
