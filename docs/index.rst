The State of housing in the Boston area
=======================================

.. raw:: html

   <!--
   Table of contents goes here
   -->

Overview:
---------

This project attempts to paint a picture using data pulled from `The
Boston
Foundation <https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single>`__
on the housing crisis as it pertains to:

-  Single Family Home Prices (Jan-June 2021, Jan-June 2022)
-  Median Condo Prices (2021-2022)
-  Share of those owners being Black or Latino

What is going to be highlighted:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There will be a couple of parts to this project:

1. Obtaining the data
2. Exploring the data for any inconsistencies/missing values.
3. Cleaning the data (If Needed)
4. Presenting the data in a way that showcases the true nature of the
   Real Estate/Job market

What I Hope To Accomplish:
~~~~~~~~~~~~~~~~~~~~~~~~~~

The data is the data, I will not be manipulating the values input, I am
doing this out in the open and citing my sources because transparency is
key with matters like this. This data can be used by first time home
buyers, flippers and wealthy folks looking to park their money in super
expensive real estate. It’s really not up to me or anyone to decide what
to do with this kind of information.

Some reference:
~~~~~~~~~~~~~~~

The data being collected for this is pretty vague, there are some key
points missing like (but not limited to): size of home in sq ft/meters,
amount of bedrooms/bathrooms, year the home was built etc.

But below I will be listing the relevant data associated with these data
sets.

The first 5 rows of each dataset

‘Single Family Median Home Data’
''''''''''''''''''''''''''''''''

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
'''''''''''''''''''''''''

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
'''''''''''''''''''''''''''''''''''''''

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

.. _single-family-median-home-data-1:

‘Single Family Median Home Data’
''''''''''''''''''''''''''''''''

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

.. _condo-median-price-data-1:

‘Condo Median Price Data’
'''''''''''''''''''''''''

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

.. _share-of-owners-being-black-or-latino-1:

‘Share of Owners Being Black or Latino’
'''''''''''''''''''''''''''''''''''''''

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

Single Family Median Price:
'''''''''''''''''''''''''''

::

   - Municipality  
   - Communities Type  
   - Median Sale Price, Jan - June 2021    
   - Median Sale Price, Jan - June 2022    
   - % Change

Condo Median price:
'''''''''''''''''''

::

   - Town
   - Community Type
   - Condo.2021
   - Condo.2022
   - Condo.PercChange

Share of Black and Latino Owners:
'''''''''''''''''''''''''''''''''

::

   - Municipality
   - Community Type
   - Percent of Home Loans to Black and Latino Buyers

.. raw:: html

   <!--
   citations go here
   - https://www.tbf.org/news-and-insights/reports//2022/October/2022%20Greater%20Boston%20Housing%20Report%20Card/2022%20GBHRC%20Charts#single
   _ 
   -->
