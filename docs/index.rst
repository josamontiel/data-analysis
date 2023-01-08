The State of housing in the Boston area
=======================================

.. raw:: html

   <!--
   Table of contents goes here
   -->

Overview
--------

This project attempts to paint a picture using data pulled from `The
Boston
Foundation <https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single>`__
on the housing crisis as it pertains to:

-  Single Family Home Prices (Jan-June 2021, Jan-June 2022)
-  Median Condo Prices (2021-2022)
-  Share of those owners being Black or Latino

What is going to be highlighted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When I first began this project, I wanted this notebook to cover
everything it possible could with regards to the data. But upon further
review, I only want/need it to do TWO things:

1. Show the top 5 and bottom 5 Cities/Towns that experienced the
   greatest change
2. Show which community type experienced the most growth.

What I Hope To Accomplish
-------------------------

The overall theme of this project is to present and visualize the data
in such a way that the end user will be able to clearly see the two main
points which are the focus of this notebook.

Some reference
--------------

The data being collected for this is pretty vague, there are some key
points missing like (but not limited to): size of home in sq ft/meters,
amount of bedrooms/bathrooms, year the home was built etc.

But below I will be listing the relevant data associated with these data
sets.

General overview of each dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

‘Single Family Median Home Data’

+-----------------+-----------------+-----------------+-----------------+
| index           | Median Sale     | Median Sale     | % Change        |
|                 | Price, Jan -    | Price, Jan -    |                 |
|                 | June 2021       | June 2022       |                 |
+=================+=================+=================+=================+
| count           | 147.0           | 147.0           | 147.0           |
+-----------------+-----------------+-----------------+-----------------+
| mean            | 72              | 80,5912.25      | 10.             |
|                 | 1655.5782312925 |                 | 787755102040816 |
+-----------------+-----------------+-----------------+-----------------+
| std             | 38              | 47              | 9.              |
|                 | 0077.9777155671 | 4227.2235190462 | 580144263214294 |
+-----------------+-----------------+-----------------+-----------------+
| min             | 347500.0        | 370250.0        | -21.2           |
+-----------------+-----------------+-----------------+-----------------+
| 25%             | 491250.0        | 547000.0        | 5.65            |
+-----------------+-----------------+-----------------+-----------------+
| 50%             | 615000.0        | 660000.0        | 11.2            |
+-----------------+-----------------+-----------------+-----------------+
| 75%             | 801250.0        | 865000.0        | 15.6            |
+-----------------+-----------------+-----------------+-----------------+
| max             | 3462500.0       | 4400000.0       | 44.4            |
+-----------------+-----------------+-----------------+-----------------+

The first 5 rows of each dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

‘Single Family Median Home Data’

+-----------+-----------+-----------+-----------+-----------+-----------+
| index     | Mun       | Co        | Median    | Median    | % Change  |
|           | icipality | mmunities | Sale      | Sale      |           |
|           |           | Type      | Price,    | Price,    |           |
|           |           |           | Jan -     | Jan -     |           |
|           |           |           | June 2021 | June 2022 |           |
+===========+===========+===========+===========+===========+===========+
| 0         | Boston    | Metro     | 3462500   | 4400000   | 27.1%     |
|           |           | Core      |           |           |           |
|           |           | Co        |           |           |           |
|           |           | mmunities |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 1         | Cambridge | Metro     | 1537500   | 1775000   | 15.4%     |
|           |           | Core      |           |           |           |
|           |           | Co        |           |           |           |
|           |           | mmunities |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 2         | Lowell    | Regional  | 415000    | 439000    | 5.8%      |
|           |           | Urban     |           |           |           |
|           |           | Centers   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 3         | Brockton  | Regional  | 377500    | 430000    | 13.9%     |
|           |           | Urban     |           |           |           |
|           |           | Centers   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 4         | Quincy    | Regional  | 605000    | 640000    | 5.8%      |
|           |           | Urban     |           |           |           |
|           |           | Centers   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+

‘Condo Median Price Data’

+-------+-----------+------------------------+------------+------------+------------------+
| index | Town      | Community Type         | Condo.2021 | Condo.2022 | Condo.PercChange |
+=======+===========+========================+============+============+==================+
| 0     | Abington  | Developing Suburbs     | 349000     | 400000     | 14.60%           |
+-------+-----------+------------------------+------------+------------+------------------+
| 1     | Acton     | Maturing Suburbs       | 370000     | 376000     | 1.60%            |
+-------+-----------+------------------------+------------+------------+------------------+
| 2     | Amesbury  | Regional Urban Centers | 340000     | 360500     | 6.00%            |
+-------+-----------+------------------------+------------+------------+------------------+
| 3     | Andover   | Developing Suburbs     | 374995     | 455000     | 21.30%           |
+-------+-----------+------------------------+------------+------------+------------------+
| 4     | Arlington | Streetcar Suburbs      | 695000     | 812500     | 16.90%           |
+-------+-----------+------------------------+------------+------------+------------------+

‘Share of owners being Black or Latino’

+-----------------+-----------------+-----------------+-----------------+
| index           | Municipality    | Community Type  | Percent of Home |
|                 |                 |                 | Loans to Black  |
|                 |                 |                 | and Latino      |
|                 |                 |                 | Buyers          |
+=================+=================+=================+=================+
| 0               | Boston          | Metro Core      | 10.9%           |
|                 |                 | Communities     |                 |
+-----------------+-----------------+-----------------+-----------------+
| 1               | Cambridge       | Metro Core      | 4.6%            |
|                 |                 | Communities     |                 |
+-----------------+-----------------+-----------------+-----------------+
| 2               | Lowell          | Regional Urban  | 27.1%           |
|                 |                 | Centers         |                 |
+-----------------+-----------------+-----------------+-----------------+
| 3               | Brockton        | Regional Urban  | 65.9%           |
|                 |                 | Centers         |                 |
+-----------------+-----------------+-----------------+-----------------+
| 4               | Quincy          | Regional Urban  | 5.1%            |
|                 |                 | Centers         |                 |
+-----------------+-----------------+-----------------+-----------------+

The last 5 rows of each dataset
'''''''''''''''''''''''''''''''

‘Single Family Median Home Data’

+-----------+-----------+-----------+-----------+-----------+-----------+
| index     | Mun       | Co        | Median    | Median    | % Change  |
|           | icipality | mmunities | Sale      | Sale      |           |
|           |           | Type      | Price,    | Price,    |           |
|           |           |           | Jan -     | Jan -     |           |
|           |           |           | June 2021 | June 2022 |           |
+===========+===========+===========+===========+===========+===========+
| 142       | Essex     | D         | 625750    | 670000    | 7.1%      |
|           |           | eveloping |           |           |           |
|           |           | Suburbs   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 143       | Dunstable | D         | 617500    | 690000    | 11.7%     |
|           |           | eveloping |           |           |           |
|           |           | Suburbs   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 144       | Nahant    | Maturing  | 805000    | 1030000   | 28.0%     |
|           |           | Suburbs   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 145       | Ashby     | Rural     | 350000    | 370250    | 5.8%      |
|           |           | Towns     |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| 146       | Plympton  | D         | 487500    | 525000    | 7.7%      |
|           |           | eveloping |           |           |           |
|           |           | Suburbs   |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+

‘Condo Median Price Data’

+-------+----------+----------+----------+----------+----------+
| index | Town     | C        | Co       | Co       | Condo.Pe |
|       |          | ommunity | ndo.2021 | ndo.2022 | rcChange |
|       |          | Type     |          |          |          |
+=======+==========+==========+==========+==========+==========+
| 142   | Wi       | Maturing | 477000   | 635000   | -34      |
|       | lmington | Suburbs  |          |          |          |
+-------+----------+----------+----------+----------+----------+
| 143   | Wi       | Maturing | 650000   | 765000   | 17.70%   |
|       | nchester | Suburbs  |          |          |          |
+-------+----------+----------+----------+----------+----------+
| 144   | Winthrop | S        | 465000   | 505000   | 8.60%    |
|       |          | treetcar |          |          |          |
|       |          | Suburbs  |          |          |          |
+-------+----------+----------+----------+----------+----------+
| 145   | Woburn   | Regional | 480000   | 525000   | 9.40%    |
|       |          | Urban    |          |          |          |
|       |          | Centers  |          |          |          |
+-------+----------+----------+----------+----------+----------+
| 146   | Wrentham | De       | 413000   | 748372   | 81.20%   |
|       |          | veloping |          |          |          |
|       |          | Suburbs  |          |          |          |
+-------+----------+----------+----------+----------+----------+

‘Share of Owners Being Black or Latino’
                                       

+-----------------+-----------------+-----------------+-----------------+
| index           | Municipality    | Community Type  | Percent of Home |
|                 |                 |                 | Loans to Black  |
|                 |                 |                 | and Latino      |
|                 |                 |                 | Buyers          |
+=================+=================+=================+=================+
| 142             | Essex           | Developing      | 0.0%            |
|                 |                 | Suburbs         |                 |
+-----------------+-----------------+-----------------+-----------------+
| 143             | Dunstable       | Developing      | 2.0%            |
|                 |                 | Suburbs         |                 |
+-----------------+-----------------+-----------------+-----------------+
| 144             | Nahant          | Maturing        | 7.7%            |
|                 |                 | Suburbs         |                 |
+-----------------+-----------------+-----------------+-----------------+
| 145             | Ashby           | Rural Towns     | 12.0%           |
+-----------------+-----------------+-----------------+-----------------+
| 146             | Plympton        | Developing      | 6.1%            |
|                 |                 | Suburbs         |                 |
+-----------------+-----------------+-----------------+-----------------+

What we know so far
-------------------

As of today (8 January 2023) we uncovered from the data that the
communities that experienced the overall greatest growth for single
family homes have been, unsurprisingly from the Metro Core Communities.
They experienced and mean growth in sales price of 20.76%. The best
performing market out of all of these communities has been Somerville
(*gang gang*), who experienced a 44% bump in median sales for single
family homes.

**The second best performing community type was the Street Car
Suburbs.**

This included Cities/Towns like:

-  Brookline
-  Arlington
-  Medford
-  Winthrop

The top performing City was Brookline coming in at a strong 37.4%
increase in sale price. Whereas Watertown, a City just 5 miles, only
experienced a 1.6% increase in sales prices.

It is when we get to the Developing Suburbs that things get interesting
as we see a lot of Towns experiencing a large negative drop in their
sales for single family homes. Rockport, in particular, experienced a
-21.2% drop in their single family home prices between 2021 and 2022.
This may be attractive to buyers looking to move out to the burbs for
some quiet and maybe larger property allocation compared to a city near
Boston.
