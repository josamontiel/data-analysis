#Import relevant libs
import pandas as pd
from pandas import read_csv
import numpy as np
import matplotlib as plt

single_family_data = pd.read_csv('./boston-housing-data-21-22/single_family_home.csv')
condo_data = pd.read_csv('./boston-housing-data-21-22/median_condo_price.csv')
black_and_latino_data = pd.read_csv('./boston-housing-data-21-22/black_and_latino_mortgage_rates.csv')