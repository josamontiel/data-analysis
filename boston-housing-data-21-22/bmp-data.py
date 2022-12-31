#Import relevant libs

import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib as plt

single_family_data = read_csv('single_family_home.csv')
condo_data = read_csv('median_condo_price.csv')
black_and_latino_data = read_csv('black_and_latino_mortgage_rates.csv')

# Print first 5 rows of values
print(single_family_data.head())
print(condo_data.head())
print(black_and_latino_data.head())

# Print last 5 rows of values
print(condo_data.tail())
print(condo_data.tail())
print(black_and_latino_data.tail())
