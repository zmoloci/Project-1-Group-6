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


<img width="918" alt="Table 1 - 1970 Population Density and Land Area by County" src="https://user-images.githubusercontent.com/120351966/220817490-bcc90dff-94ca-4b59-8b0a-f2687bafe62a.png">
<img width="918" alt="Table 1 - 2020 Population Density and Land Area by County" src="https://user-images.githubusercontent.com/120351966/220817503-4694fd01-6c83-4e0d-884f-6142eb4c26eb.png">
<img width="635" alt="bin4_histogram" src="https://user-images.githubusercontent.com/120351966/220822155-a3b33435-201b-47ad-8b9e-d5b24f8ed751.png">

<img width="918" alt="Table 1 - 1970 Population Density and Land Area by County - With BIN4" src="https://user-images.githubusercontent.com/120351966/220817519-dc656660-1929-4751-a4de-8c6a52d7419f.png">
<img width="918" alt="Table 1 - 2020 Population Density and Land Area by County - With BIN4" src="https://user-images.githubusercontent.com/120351966/220817533-295e41d8-664f-47ad-8252-214b695a10f5.png">


<img width="749" alt="Pop_den_County_Map_2020" src="https://user-images.githubusercontent.com/120351966/220798793-4e833f99-1893-4758-8185-5f6372e6341f.png">




#### Does population density growth affect population growth?

<img width="918" alt="NY_50yr_Pop_grow_vs_1970_PopDens" src="https://user-images.githubusercontent.com/120351966/220523815-cc34ecae-647f-49eb-bb13-a5269de36bea.png">



#### Does population density affect income?
![2020_NY_County_PCI](https://user-images.githubusercontent.com/120351966/220819106-5b1ec52c-6f4c-491e-823a-6e3ea9191a51.png)

![2020_NY_County_PCI_sort_by_1970_popdens](https://user-images.githubusercontent.com/120351966/220806410-9512d917-822e-4a73-8cd0-5f63ab1c45e8.png)


<img width="919" alt="NY_percapitaincome_2020_vs_1970_PopDens" src="https://user-images.githubusercontent.com/120351966/220523742-a27b8469-cfbb-4ee6-b9aa-84955050d5dd.png">





![NY_Albany_Pop_Income_Growth](https://user-images.githubusercontent.com/120351966/220797974-d3c3dc59-fcfc-4fe2-8f55-bef220a18c10.png)

![Albany_County_growth_pc](https://user-images.githubusercontent.com/120351966/220820778-e0621051-4a8a-494c-8657-5788b8b97259.png)
![NY_growth_pc](https://user-images.githubusercontent.com/120351966/220822303-96d4dd87-691a-4b3d-bd20-099413d7b105.png)

![Albany_growth_correlation](https://user-images.githubusercontent.com/120351966/220820802-3741bad9-c6d4-4450-b88e-13e6fc590ba6.PNG)
![NYstate_growth_correlation](https://user-images.githubusercontent.com/120351966/220822429-dd20c5b1-0020-4b5d-9e41-8252cfa6df82.PNG)

![Highest_pop_growthcounty_cor](https://user-images.githubusercontent.com/120351966/220822262-c6d7e0a5-ae67-48ea-b3da-2cf0d054fa54.PNG)
![Lowest_pop_growthcounty_cor](https://user-images.githubusercontent.com/120351966/220822277-d88aea83-f572-4522-a2d1-c52dae4251de.PNG)

### Conclusion


