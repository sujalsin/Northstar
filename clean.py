import json
import pandas as pd

with open('/Users/robby/Downloads/NS_dataset.jsonc') as f:
    data = json.load(f)



df = pd.DataFrame(columns=["authors", "abstract"])

for i in range(len(data)):
    currentItem = data[i]
    df.loc[i] = [data[i]["authors"], data[i]["abstract"]]
print(df)