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

 Single Family Median Price:
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
```
<!--
citations go here
- https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single
_ 
-->
