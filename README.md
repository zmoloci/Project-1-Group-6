# Project-1-Group-6
# Data Analytics Bootcamp: Project 1


## Group 6


### DAY 0
Project Ideas:

Lailah: Using: statcan.gc.ca (CPI), https://api.canada.ca/en/homepage




Zac: Using: https://www.census.gov/data/developers/data-sets/decennial-census.html for New York State? (or all states??)

How has the population density of counties changed over time (2000-2020)?
Do low popden counties’ pop increase at a relatively high rate vs. high popden counties?
Categorize counties based on low, high popdensity
Population increase from 2000 to 2020 based on initial popdensity bin (correlations: low initial popdensity correlates with high rate of population increase? vice-versa)

Has salary in low pop. density counties increased at a relatively high rate versus salary in high pop. density counties from 2000 to 2020?
Versus High popden counties, do Low popden counties have a relatively low avg. salary? Median salary?

Discussion/Future Research:
How does affordability factor in?




Include:
Heat map style plot for pop. increase rates by county over period 2000-2020
Heat map style plot for average salary by county over period 2000-2020
Also, scatterplot with unique markers based on popdensity bin (very low = triangle, etc.)
Heat map style plot for median salary by county over period 2000-2020
Also, scatterplot with unique markers based on popdensity bin (very low = triangle, etc.)
Bar graph of population by county by year (2000, 2010, 2020) grouped by 2000 popdensity bin (very low, low, medium, high, very high)
Bar graph of population change rate (pop change / years) by county (2010 and 2020) by popdensity bin





Priya:
https://www.kaggle.com/
https://www.census.gov/data/developers/data-sets/decennial-census.html


---

### DAY 1

#### Forecasting Population Growth in New York State by County: "Moving to the country?"

- **How does initial population density affect growth rates?**
- **Who is interested in this data?**
  - **Car dealerships:**
    - opening a new location?
    - Car ownership data?
    - Salary data?
    
  - **Realtors:** 
    - Where is the next hot market?
    - Housing price increase hot spots?
    - Markets in decline? Pricing/availability decline?
    - Which type of dwelling in most popular/most needed (Single-detached, semi-detached, condo, etc.)?
    - Demographic changes (more young families moving in vs. retirees?)
    
  - **Retailers/Grocers:**
    - Which county needs a(nother) strip mall? 
    - Food terminals? 
    - Distance from nearest shipping ports? 
    - Transportation infrastructure data?
    
  - **Employees:** 
    - Where to start our family? 
    - Salary/revenue averages within a county.
    - Could include crime data, housing prices, poverty statistics.
  

#### Data Sources

- Decennial Census (2020, 2010, 2000) from census.gov (https://www.census.gov/data/developers/data-sets/decennial-census.html)

- Economic Census (2017, 2012, 2007, 2002) from census.gov (https://www.census.gov/data/developers/data-sets/economic-census.html)
  - *The Economic Census is the official measure of the Nation’s businesses and economy. Conducted every five years, the survey serves as the statistical benchmark for current economic activity, such as, the Gross Domestic Product and the Producer Price Index.*
  - *Data collected from individual business establishments on physical location, type of business activity (industry), employment, payroll, and revenue by type of service or product and more provides vital information on the changes in the ownership and organizational structure of American Businesses and industries. Some inquiries apply to certain industries but not others, such as, materials consumed and franchising.*
  - *Economic Census data is important to everyone. Examples include businesses using the data to make decisions about where to locate, local communities use the data to attract new businesses and individuals use the data to identify emerging markets.*

- Annual Survey of Entrepreneurs from census.gov (https://www.census.gov/data/developers/data-sets/ase.html)
  - **Company Summary.**  *Provides data for employer businesses by sector, sex, ethnicity, race, veteran status, years in business, receipts size of firm, and employment size of firm for the U.S., states, and the fifty most populous metropolitan statistical areas (MSAs).*
  - **Characteristics of Businesses.**  *Provides data for employer firms by sector, sex, ethnicity, race, veteran status, and years in business for the U.S., states, and fifty most populous MSAs, including detailed business characteristics.*
  - **Characteristics of Business Owners.**  *Provides data for owners of respondent employer firms by sector, sex, ethnicity, race, veteran status, and years in business for the U.S., states, and top fifty most populous MSAs, including detailed owner characteristics.*

#### Analysis Question

**Categorize Counties by Population Density**
  - population
  - area (square mile)
  - or just Population Density if available

**Is population growing?**
  - population by county (2000, 2010, 2020 or even by year if easily accessible)

**Is population growth higher/lower than national/state average?**
  - find data for pop growth on national/state scale over similar period as above (county scale)

**Is salary increasing or decreasing (Top 5 Industry over a sample of counties - low density, high density)?**
  - mean, median salary by county
  - If data is only available by industry, then how do we calculate whole population level salary?
  - Do we just use median salary over top 5 industries in each county?
    - 

**Does this differ from national/state averages?**

**Does this effect correlate to each county's intial / final population density?**
  - correlation matrix (graph)
  
  
##Before Class on Monday let's touch base on where we are for Assignment 6
 - Are we stuck? Errors?
 - Zac has tutoring session Monday night at 10pm and can try to work through some errors, roadblocks, etc. related to Asssignment 6##




#### Visualizations


Include:
Heat map style plot for pop. increase rates by county over period 2000-2020
Heat map style plot for average salary by county over period 2000-2020
Also, scatterplot with unique markers based on popdensity bin (very low = triangle, etc.)
Heat map style plot for median salary by county over period 2000-2020
Also, scatterplot with unique markers based on popdensity bin (very low = triangle, etc.)
Bar graph of population by county by year (2000, 2010, 2020) grouped by 2000 popdensity bin (very low, low, medium, high, very high)
Bar graph of population change rate (pop change / years) by county (2010 and 2020) by popdensity bin



#### Project Plan

Before Sunday Feb. 6 meeting (8pm EST):
 - Lailah try to make a list of variables that we will need to pull from the APIs that we have decided on or others

During day Monday-Thurs
  - Zac/Priya building code to pull variables/data that Lailah has highlighted




