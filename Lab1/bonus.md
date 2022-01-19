# Bonus A
### Importing Essential Libraries
```
import numpy as np # Library for Numeric Computations in Python
import pandas as pd # Library for Data Acquisition and Preparation
import seaborn as sb # Higher-level library for Data Visualization
# import matplotlib as mp # Low-level library for Data Visualization

import matplotlib.pyplot as plt # we only need pyplot
# sb.set() # set the default Seaborn style for graphics
```

### Importing Census Income CSV Dataset
```
income_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', names=["Age", "Work Class", "fntwgt", "Education", "Education-num", "Marital Status",  "Occupation", "Relationship", "Race",  "Sex", "Capital Gain", "Capital Loss", "Hours per Week", "Native Country","Income"])
```

```
print("Data Number of Tables: ", len(income_data))
income_data

print("Data Shape: ", income_data.shape)

print(income_data.info())

# print(income_data.describe())
income_data.describe()
```
# Bonus B
### Importing Essential Libraries
```
import numpy as np # Library for Numeric Computations in Python
import pandas as pd # Library for Data Acquisition and Preparation
import seaborn as sb # Higher-level library for Data Visualization
# import matplotlib as mp # Low-level library for Data Visualization

import matplotlib.pyplot as plt # we only need pyplot
# sb.set() # set the default Seaborn style for graphics
```
### Importing Olympic 2000 to 2016 HTML Data
```
for years in range(2000, 2017, 4):
    data_link = 'https://en.wikipedia.org/wiki/'+ str(years) + '_Summer_Olympics_medal_table'
    olympic_data = pd.read_html(data_link)
    
    medal_table = pd.DataFrame(olympic_data[2][:86])
    print(years)
    display(medal_table.head(20))
```
