# Problem 1
### Importing Essential Libraries
import numpy as np # Library for Numeric Computations in Python
import pandas as pd # Library for Data Acquisition and Preparation

### (a) Importing "train.csv" Data
# train_data = pd.read_csv('train.csv', header = None)
train_data = pd.read_csv('train.csv')
# train_data.head()
train_data

### (b) Checking number of Rows & Variables
print("Data Shape: ", train_data.shape)
print("Number of Rows: ", len(train_data))
print("Number of Columns: ", len(train_data.columns))

### (c) Checking Data Types (Numeric/Categorical)
# print(train_data.dtypes)
train_data.dtypes
print(train_data.columns)

### (d) .info() Method
# print(train_data.info())
train_data.info()

### (e) .describe() Method
# print(train_data.describe())
train_data.describe()

# Problem 2
### Importing Essential Libraries
import numpy as np # Library for Numeric Computations in Python
import pandas as pd # Library for Data Acquisition and Preparation
import seaborn as sb # Higher-level library for Data Visualization
# import matplotlib as mp # Low-level library for Data Visualization

import matplotlib.pyplot as plt # we only need pyplot
# sb.set() # set the default Seaborn style for graphics

### (a) Importing Wikipedia HTML Data
olympic_data = pd.read_html('https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table')

### (b) Checking number of Tables
# print("Data Type: ", type(olympic_data))
print("Data Number of Tables: ", len(olympic_data))

### (c) Finding Actual Medal Table
olympic_data[2].head()

### (d) Extracting Medal Table as New Pandas DataFrame
medal_table = pd.DataFrame(olympic_data[2][:86])
# medal_table.head()
medal_table

### (e) Extracting Top 20 Countries from Medal Table as New DataFrame
top_countries = pd.DataFrame(medal_table['NOC'])
top_countries.head(n=20)
