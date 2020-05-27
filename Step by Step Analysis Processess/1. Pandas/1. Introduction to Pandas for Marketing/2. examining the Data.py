# Import pandas into the environment
import pandas as pd

# Import marketing.csv 
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/PYTHON/Analyzing Marketing Campaigns with Pandas/DATA/Marketing1.csv')

#marketing.drop(marketing.columns[0], axis = 1)
#del marketing['No']

# Print the first five rows of the DataFrame
#print(marketing.head())

# Print the statistics of all columns
#print(marketing.describe())

# Check column data types and non-missing values
print(marketing.info())
print(marketing.head())
