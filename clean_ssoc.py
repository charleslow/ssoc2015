import pandas as pd

def clean_string(text):
    text = text.split()
    text = " ".join(text)
    return text

with open("ssoc2015.csv") as f:
    data = f.readlines()

data = pd.read_csv("ssoc2015.csv")
data.columns = ["ssoc_2015", "ssoc_2015_title", "a", "b"]
data = data[~pd.isna(data["ssoc_2015_title"]) | ~pd.isna(data["ssoc_2015"])]
data = data[["ssoc_2015", "ssoc_2015_title"]].reset_index(drop=True)
data["ssoc_2015_title"] = data["ssoc_2015_title"].map(lambda x: x.title())


ssoc_dict = {}
curr_title = []
for i in reversed(range(data.shape[0])):
    code = data.loc[i, "ssoc_2015"]
    title = data.loc[i, "ssoc_2015_title"]
    curr_title.append(title)
    if not pd.isna(code):
        curr_title = reversed(curr_title)
        ssoc_dict[code] = clean_string(" ".join(curr_title))
        curr_title = []

ssoc_codes = []
ssoc_titles = []
for k,v in reversed(ssoc_dict.items()):
    ssoc_codes.append(k)
    ssoc_titles.append(v)
df = pd.DataFrame({"ssoc_2015": ssoc_codes, "ssoc_2015_title": ssoc_titles})
df.to_csv("ssoc_2015_titles.csv")