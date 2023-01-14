# The State of housing in the Boston area

> Note: I do my best to have the documentation site mirror the readme, please bear with me if there are inconsistencies, I know about them I just havent corrected them as of yet. 

![image](https://user-images.githubusercontent.com/91287801/212477320-4e8b030a-4651-4edc-b531-99f5a01e8b43.png)
###### image credit [Dave Thompsen](https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/zakim-bridge-dave-thompsen.jpg)

<!--
Table of contents goes here
-->
## Overview

As we all know, the cost of living has gone up, substantially. Every sector has been affected on some level. Most notable (not because of value, more to do with the fact that we all need a roof over our heads) is the real estate sector.

As someone who is from the Boston, MA area, and someone who is in Data Science, I feel compelled to decicate some time and energy to giving some insight into the housing market in the area I grew up in. I am personally someone who was a victim of the rising price of real estate in the Boston, area. I was not the first and I wasn't the last person to feel the effects of the rising cost of living and the real estate boom.

If you would like to see where I pulled some of the data from, check it out [here](https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts)

The datasets I will be working with are listed below:

* Single Family Home Prices (Jan-June 2021, Jan-June 2022)
* Median Condo Prices (2021-2022)
* Share new mortgages going to those being Black or Latino
* Eviction Rates

### What is going to be highlighted

This particular project is only going to highlight one thing, the community types who experienced the greatest changes (both positive and negative %). I chose this due to the fact that while, Boston may have higher prices than say Somerville, Somerville experienced a greater increase percentage than Boston. The pct increase, in my opinion, has a far greater impact on individuals than the sell/buy prices.

## The community types for this survey were as follows

- Metro Core Communities (Inner Cities)
- Regional Urban Centers
- Street Car Suburbs
- Developing Suburbs
- Maturing Suburbs
- Rural Towns

## What we know so far

As of today (8 January 2023) we uncovered from the data that the communities that experienced the overall greatest growth for single family homes have been, unsurprisingly from the Metro Core Communities. They experienced and mean growth in sales price of 20.76%. The best performing market out of all of these communities has been Somerville (*gang gang*), who experienced a 44% bump in median sales for single family homes.

**The second best performing community type was the Street Car Suburbs.**

This included Cities/Towns like:

* Brookline
* Arlington
* Medford
* Winthrop

The top performing City was Brookline coming in at a strong 37.4% increase in sale price. Whereas Watertown, a City just 5 miles, only experienced a 1.6% increase in sales prices.

It is when we get to the Developing Suburbs that things get interesting as we see a lot of Towns experiencing a large negative drop in their sales for single family homes. Rockport, in particular, experienced a -21.2% drop in their single family home prices between 2021 and 2022. This may be attractive to buyers looking to move out to the burbs for some quiet and maybe larger property allocation compared to a city near Boston.

#### Overview of data by Community type for Single Family Homes

*Metro Core Communites*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|7|7|7|
|mean|1,135,660\.71|1,399,028\.57|20\.75|
|std|1,091,096\.59|1,397,197\.62|12\.92|
|min|476,500|577,450|8\.6|
|25%|531,000|605,375|11\.25|
|50%|580,000|630,000|15\.4|
|75%|1,184,312\.50|1,487,500|27\.2|
|max|3,462,500|4,400,000|44\.4|

*Regional Urban Centers*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|17|17|17|
|mean|520102\.95|567195\.24|9\.47|
|std|102287\.48|103337\.72|4\.59|
|min|360000|413000|-0\.8|
|25%|445000|500000|5\.8|
|50%|529000|590000|10\.3|
|75%|600000|620000|13\.3|
|max|750000|815000|15\.7|

*StreetCar Suburbs*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|9|9|9|
|mean|1039227\.78|1198755\.56|12\.99|
|std|439110\.74|611463\.45|10\.78|
|min|629000|694900|1\.6|
|25%|728050|802500|7\.4|
|50%|790000|850000|9\.7|
|75%|1441500|1575900|14\.3|
|max|1850000|2542000|37\.4|

*Developing Suburbs*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|65\.0|65\.0|65\.0|
|mean|636039\.2307692308|687538\.4615384615|8\.86923076923077|
|std|225127\.9869478949|242892\.57990436052|10\.234316096424736|
|min|347500|400000|-21\.2|
|25%|461000|517500|3\.6|
|50%|583450|622500|9\.5|
|75%|747500|764500|14\.5|
|max|1425000|1631500|33\.5|

*Rural Town*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|1|1|1|
|mean|350000\.0|370250\.0|5\.8|
|std|NaN|NaN|NaN|
|min|350000\.0|370250\.0|5\.8|
|25%|350000\.0|370250\.0|5\.8|
|50%|350000\.0|370250\.0|5\.8|
|75%|350000\.0|370250\.0|5\.8|
|max|350000\.0|370250\.0|5\.8|

> There is no table for Maturing Suburbs as there is no data for them

# What we know so far

### Single Family Homes

Currently, from the data we can see the communities that experienced the overall greatest growth for single family homes have been, unsurprisingly from the Metro Core Communities. They experienced and mean growth in sales price of 20.76%. The best performing market out of all of these communities has been Somerville (*gang gang*), who experienced a 44% bump in median sales for single family homes between Jan-Jun 2021-2022.

**The second best performing community type was the Street Car Suburbs.**

This included Cities/Towns like:

* Brookline
* Arlington
* Medford
* Winthrop

The top performing City was Brookline coming in at a strong 37.4% increase in sale price. Whereas Watertown, a City just 5 miles away, only experienced a 1.6% increase in sales prices. Interesting to see, to say the least.

It is when we get to the Developing Suburbs that things get interesting as we see a lot of Towns experiencing a large negative drop in their sales for single family homes. Rockport, in particular, experienced a -21.2% drop in their single family home prices between 2021 and 2022. This may be attractive to buyers looking to move out to the burbs for some quiet and maybe larger property allocation compared to a city near Boston.

<!-- ![Sheet 1](https://user-images.githubusercontent.com/91287801/211865276-34263adc-f6b3-4c1f-9f2b-871a4813b18d.png) -->

![Sheet 1(1)](https://user-images.githubusercontent.com/91287801/212280192-28ed6c94-0a9b-493a-ad0c-b66428962b10.png)
<!--
citations go here
- https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single
_ 
-->
