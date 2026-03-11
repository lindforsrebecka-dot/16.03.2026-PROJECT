import pandas as pd

df = pd.read_csv("data/raw/guardian_articles.csv")

print(df["section"].value_counts())

world_df = df[df["section"] == "World news"]
sport_df = df[df["section"] == "Sport"]
culture_df = df[df["section"] == "Culture"]

world_df.to_csv("data/processed/world_articles.csv", index=False)
sport_df.to_csv("data/processed/sport_articles.csv", index=False)
culture_df.to_csv("data/processed/culture_articles.csv", index=False)

print("World:", len(world_df))
print("Sport:", len(sport_df))
print("Culture:", len(culture_df))