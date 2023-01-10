# The State of housing in the Boston area

<!--
Table of contents goes here
-->
## Overview

This project attempts to paint a picture using data pulled from [The Boston Foundation](https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single) on the housing crisis as it pertains to:

* Single Family Home Prices (Jan-June 2021, Jan-June 2022)
* Median Condo Prices (2021-2022)
* Share of those owners being Black or Latino

### What is going to be highlighted

When I first began this project, I wanted this notebook to cover everything it possible could with regards to the data. But upon further review, I only want/need it to do TWO things:

1. Show the top 5 and bottom 5 Cities/Towns that experienced the greatest change
2. Show which community type experienced the most growth.

## What I Hope To Accomplish

The overall theme of this project is to present and visualize the data in such a way that the end user will be able to clearly see the two main points which are the focus of this notebook.

## Some reference

The data being collected for this is pretty vague, there are some key points missing like (but not limited to): size of home in sq ft/meters, amount of bedrooms/bathrooms, year the home was built etc.

But below I will be listing the relevant data associated with these data sets.

### General overview of each dataset

'Single Family Median Home Data'

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|147\.0|147\.0|147\.0|
|mean|721655\.5782312925|80\,5912\.25|10\.787755102040816|
|std|380077\.9777155671|474227\.2235190462|9\.580144263214294|
|min|347500\.0|370250\.0|-21\.2|
|25%|491250\.0|547000\.0|5\.65|
|50%|615000\.0|660000\.0|11\.2|
|75%|801250\.0|865000\.0|15\.6|
|max|3462500\.0|4400000\.0|44\.4|

#### The first 5 rows of each dataset

'Single Family Median Home Data'

|index|Municipality|Communities Type|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|---|---|
|0|Boston|Metro Core Communities|3462500|4400000|27\.1%|
|1|Cambridge|Metro Core Communities|1537500|1775000|15\.4%|
|2|Lowell|Regional Urban Centers|415000|439000|5\.8%|
|3|Brockton|Regional Urban Centers|377500|430000|13\.9%|
|4|Quincy|Regional Urban Centers|605000|640000|5\.8%|

'Condo Median Price Data'

|index|Town|Community Type|Condo\.2021|Condo\.2022|Condo\.PercChange|
|---|---|---|---|---|---|
|0|Abington|Developing Suburbs|349000|400000|14\.60%|
|1|Acton|Maturing Suburbs|370000|376000|1\.60%|
|2|Amesbury|Regional Urban Centers|340000|360500|6\.00%|
|3|Andover|Developing Suburbs|374995|455000|21\.30%|
|4|Arlington|Streetcar Suburbs|695000|812500|16\.90%|

'Share of owners being Black or Latino'

|index|Municipality|Community Type|Percent of Home Loans to Black and Latino Buyers|
|---|---|---|---|
|0|Boston|Metro Core Communities|10\.9%|
|1|Cambridge|Metro Core Communities|4\.6%|
|2|Lowell|Regional Urban Centers|27\.1%|
|3|Brockton|Regional Urban Centers|65\.9%|
|4|Quincy|Regional Urban Centers|5\.1%|

##### The last 5 rows of each dataset

'Single Family Median Home Data'

|index|Municipality|Communities Type|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|---|---|
|142|Essex|Developing Suburbs|625750|670000|7\.1%|
|143|Dunstable|Developing Suburbs|617500|690000|11\.7%|
|144|Nahant|Maturing Suburbs|805000|1030000|28\.0%|
|145|Ashby|Rural Towns|350000|370250|5\.8%|
|146|Plympton|Developing Suburbs|487500|525000|7\.7%|

'Condo Median Price Data'

|index|Town|Community Type|Condo\.2021|Condo\.2022|Condo\.PercChange|
|---|---|---|---|---|---|
|142|Wilmington|Maturing Suburbs|477000|635000|-34|
|143|Winchester|Maturing Suburbs|650000|765000|17\.70%|
|144|Winthrop|Streetcar Suburbs|465000|505000|8\.60%|
|145|Woburn|Regional Urban Centers|480000|525000|9\.40%|
|146|Wrentham|Developing Suburbs|413000|748372|81\.20%|

###### 'Share of Owners Being Black or Latino'

|index|Municipality|Community Type|Percent of Home Loans to Black and Latino Buyers|
|---|---|---|---|
|142|Essex|Developing Suburbs|0\.0%|
|143|Dunstable|Developing Suburbs|2\.0%|
|144|Nahant|Maturing Suburbs|7\.7%|
|145|Ashby|Rural Towns|12\.0%|
|146|Plympton|Developing Suburbs|6\.1%|

 <!-- Single Family Median Price:
```
- Municipality 
- Communities Type 
- Median Sale Price, Jan - June 2021 
- Median Sale Price, Jan - June 2022 
- % Change
```

Condo Median price:
```
- Town
- Community Type
- Condo.2021
- Condo.2022
- Condo.PercChange
```

Share of Black and Latino Owners:
```
- Municipality
- Community Type
- Percent of Home Loans to Black and Latino Buyers
``` -->

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
|count|7\.0|7\.0|7\.0|
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
|count|17\.0|17\.0|17\.0|
|mean|520102\.9411764706|567195\.2352941176|9\.46470588235294|
|std|102287\.4724590398|103337\.71569926043|4\.586521173022996|
|min|360000\.0|413000\.0|-0\.8|
|25%|445000\.0|500000\.0|5\.8|
|50%|529000\.0|590000\.0|10\.3|
|75%|600000\.0|620000\.0|13\.3|
|max|750000\.0|815000\.0|15\.7|

*StreetCar Suburbs*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|9\.0|9\.0|9\.0|
|mean|1039227\.7777777778|1198755\.5555555555|12\.988888888888889|
|std|439110\.73995570233|611463\.4476219962|10\.77548658349641|
|min|629000\.0|694900\.0|1\.6|
|25%|728050\.0|802500\.0|7\.4|
|50%|790000\.0|850000\.0|9\.7|
|75%|1441500\.0|1575900\.0|14\.3|
|max|1850000\.0|2542000\.0|37\.4|

*Developing Suburbs*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|65\.0|65\.0|65\.0|
|mean|636039\.2307692308|687538\.4615384615|8\.86923076923077|
|std|225127\.9869478949|242892\.57990436052|10\.234316096424736|
|min|347500\.0|400000\.0|-21\.2|
|25%|461000\.0|517500\.0|3\.6|
|50%|583450\.0|622500\.0|9\.5|
|75%|747500\.0|764500\.0|14\.5|
|max|1425000\.0|1631500\.0|33\.5|

*Rural Town*

|index|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|
|count|1\.0|1\.0|1\.0|
|mean|350000\.0|370250\.0|5\.8|
|std|NaN|NaN|NaN|
|min|350000\.0|370250\.0|5\.8|
|25%|350000\.0|370250\.0|5\.8|
|50%|350000\.0|370250\.0|5\.8|
|75%|350000\.0|370250\.0|5\.8|
|max|350000\.0|370250\.0|5\.8|

> There is no table for Maturing Suburbs as there is no data for them

Below is a table of the top performing municipalities by community type:

|index|Municipality|Communities Type|Median Sale Price, Jan - June 2021|Median Sale Price, Jan - June 2022|% Change|
|---|---|---|---|---|---|
|0|Somerville|Metro Core Communities|831125|1200000|44\.4|
|1|Brookline|Streetcar Suburbs|1850000|2542000|37\.4|
|2|Amesbury|Regional Urban Centers|481000|556319|15\.7|
|3|Sherborn|Developing Suburbs|955000|1275000|33\.5|
|4|Ashby|Rural Towns|350000|370250|5\.8|

<!--
citations go here
- https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single
_ 
-->
