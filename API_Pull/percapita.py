import requests
import numpy as np
import pandas as pd

years = np.arange(2000, 2021)
dates = np.array([f"{year}-01-01" for year in years])
df_list = []

dates_list = dates.tolist()

for year in dates_list:
    url_data = "https://api.stlouisfed.org/geofred/regional/data?api_key=d6c9f833698c931c8e63dd3973b55579&series_group=882&date={0}&region_type=state&units=Dollars&frequency=a&season=NSA&file_type=json".format(
        year)
    res = requests.get(url_data)
    s = res.json()
    fin = s['meta']['data'][year]
    tdf = pd.DataFrame(fin)
    tdf['year'] = year
    df_list.append(tdf)

# print(df_list)
# print(type(df_list[0]))

df = pd.concat(df_list, axis=0, ignore_index=True)
print(df)
df.to_csv("per_capita_income.csv")
