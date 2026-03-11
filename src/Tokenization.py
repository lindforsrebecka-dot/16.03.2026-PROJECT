import pandas as pd
import re
world_df = pd.read_csv("data/processed/world_articles.csv")
sport_df = pd.read_csv("data/processed/sport_articles.csv")
culture_df = pd.read_csv("data/processed/culture_articles.csv")
def tokenize(text):
    return re.findall(r"\b[a-zA-Z']+\b", str(text).lower())
world_tokens = [token for text in world_df["title"] for token in tokenize(text)]
sport_tokens = [token for text in sport_df["title"] for token in tokenize(text)]
culture_tokens = [token for text in culture_df["title"] for token in tokenize(text)]
pd.DataFrame(world_tokens, columns=["token"]).to_csv("data/processed/world_tokens.csv", index=False)
pd.DataFrame(sport_tokens, columns=["token"]).to_csv("data/processed/sport_tokens.csv", index=False)
pd.DataFrame(culture_tokens, columns=["token"]).to_csv("data/processed/culture_tokens.csv", index=False)

print("Done.")
print("World tokens:", len(world_tokens))
print("Sport tokens:", len(sport_tokens))
print("Culture tokens:", len(culture_tokens))
