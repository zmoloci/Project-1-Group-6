# Group Project 1
## Exploring the Impact of Population Density on County Population Growth Rates and Per Capita Income in New York State.

### Research Questions

- How is the population distributed in NY State?

- Does population density growth affect population growth?

- Does population density affect income?






### Analysis (and Visualizations)

#### Data Collection

- New York State Per Capita Personal Income by County for 1970-2020 was accessed via [FRED.org](https://fred.stlouisfed.org/release/tables?rid=175&eid=267974&od=2000-01-01#) and compiled using the [Python](https://www.python.org/doc/) library [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- New York State, County-Level Decennial Census Population data for 1970-2020 was accessed and downloaded via the New York State resource: [Data.NY.Gov](https://data.ny.gov/Government-Finance/Annual-Population-Estimates-for-New-York-State-and/krt9-ym2k/explore/query/SELECT%20%60fips_code%60%2C%20%60geography%60%2C%20%60year%60%2C%20%60program_type%60%2C%20%60population%60/page/filter)
- New York State Land Area by County was accessed from [Health.NY.Gov](https://www.health.ny.gov/statistics/vital_statistics/2018/table02.htm) using the [Python](https://www.python.org/doc/) library [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- New York State County Latitude and Longitude was pulled from the [GEOApify](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/#about) API using [Python](https://www.python.org/doc/)




#### How is the population distributed in NY State?
<img width="919" alt="NY_percapitaincome_2020_vs_1970_PopDens" src="https://user-images.githubusercontent.com/120351966/220523681-b76beb47-3514-4906-9164-4b638c422f4d.png">

![Table 1 - 2020 Population Density and Land Area by County](https://user-images.githubusercontent.com/120351966/220524006-547fb36f-aebf-40c1-ad93-c1c61d8b8294.png)



#### Does population density growth affect population growth?

<img width="918" alt="NY_50yr_Pop_grow_vs_1970_PopDens" src="https://user-images.githubusercontent.com/120351966/220523815-cc34ecae-647f-49eb-bb13-a5269de36bea.png">



#### Does population density affect income?


<img width="919" alt="NY_percapitaincome_2020_vs_1970_PopDens" src="https://user-images.githubusercontent.com/120351966/220523742-a27b8469-cfbb-4ee6-b9aa-84955050d5dd.png">


<img width="796" alt="1970_popdens_histogram_bin4" src="https://user-images.githubusercontent.com/120351966/220523163-f81b2f6d-7eb6-4ce0-b2c9-308b5ecddc0b.png">

![Table 1 - 1970 Population Density and Land Area by County - With BIN4](https://user-images.githubusercontent.com/120351966/220524333-da041ef8-9ac1-4ca2-8ff2-8a6bb1d4a065.png)


<img width="1136" alt="popden_mapplot_bin4" src="https://user-images.githubusercontent.com/120351966/220523532-16eeb827-f37c-48c4-9db0-c4302699a66c.png">






### Conclusion


