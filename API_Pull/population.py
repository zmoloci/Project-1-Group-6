import requests
import pandas as pd
url = "https://data.ny.gov/resource/krt9-ym2k.json?$query=SELECT%20%60fips_code%60%2C%20%60geography%60%2C%20%60year%60%2C%20%60program_type%60%2C%20%60population%60"

res =  requests.get(url)
#print(res.json())

df = pd.DataFrame(res.json())
print(df)

df.to_csv("population.csv")
