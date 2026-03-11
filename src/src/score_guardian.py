import pandas as pd
import re

world_tokens = pd.read_csv("data/processed/world_tokens.csv")
culture_tokens = pd.read_csv("data/processed/culture_tokens.csv")
sport_tokens = pd.read_csv("data/processed/sport_tokens.csv")
                                
labmt = pd.read_csv("data/raw/Hedonometer.csv")
labmt["Word"] = labmt["Word"].str.lower()
labmt = labmt.rename(columns={"Word": "token", "Happiness Score": "score"})

world_df = pd.read_csv("data/processed/world_articles.csv")
culture_df = pd.read_csv("data/processed/culture_articles.csv")
sport_df = pd.read_csv("data/processed/sport_articles.csv")



world_tokens["token"] = world_tokens["token"].str.lower()
culture_tokens["token"] = culture_tokens["token"].str.lower()
sport_tokens["token"] = sport_tokens["token"].str.lower()

world_match = world_tokens.merge(labmt, on="token", how="inner")
culture_match = culture_tokens.merge(labmt, on="token", how="inner")
sport_match = sport_tokens.merge(labmt, on="token", how="inner")

print("World matches:", len(world_match))
print("Culture matches:", len(culture_match))
print("Sport matches:", len(sport_match))

world_tokens["token"] = world_tokens["token"].astype(str).str.lower()
culture_tokens["token"] = culture_tokens["token"].astype(str).str.lower()
sport_tokens["token"] = sport_tokens["token"].astype(str).str.lower()


world_match = world_tokens.merge(labmt, on="token", how="inner")
culture_match = culture_tokens.merge(labmt, on="token", how="inner")
sport_match = sport_tokens.merge(labmt, on="token", how="inner")


print("World matched tokens:", len(world_match))
print("Culture matched tokens:", len(culture_match))
print("Sport matched tokens:", len(sport_match))


print("World happiness:", world_match["score"].mean())
print("Culture happiness:", culture_match["score"].mean())
print("Sport happiness:", sport_match["score"].mean())


world_match.to_csv("data/processed/world_matched.csv", index=False)
culture_match.to_csv("data/processed/culture_matched.csv", index=False)
sport_match.to_csv("data/processed/sport_matched.csv", index=False)

print("Done.")


