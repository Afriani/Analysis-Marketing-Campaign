# Import pandas into the environment
import pandas as pd

# Import Numpy
import numpy as np

# Import Stats
from scipy import stats

# Import t-test
from scipy.stats import ttest_ind

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv', parse_dates =['date_served', 'date_subscribed', 'date_canceled'])
#print(marketing)

# Subset the DataFrame
email = marketing[marketing['marketing_channel']=='Email']

# Group the email DataFrame by variant 
alloc = email.groupby(['variant'])['user_id'].nunique()

# Group marketing by user_id and variant
subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
subscribers_df = pd.DataFrame(subscribers.unstack(level=1)) 

# Drop missing values from the control column
control = subscribers_df['control'].dropna()

# Drop missing values from the personalization column
personalization = subscribers_df['personalization'].dropna()

def lift(a,b):
    # Calcuate the mean of a and b 
    a_mean = np.mean(control)
    b_mean = np.mean(personalization)
    
    # Calculate the lift using a_mean and b_mean
    lift = (b_mean - a_mean) / a_mean
  
    return str(round(lift*100, 2)) + '%'
  
# Print lift() with control and personalization as inputs
print('Lift = ', lift(control, personalization))

# Evaluating statistical significance
print(stats.ttest_ind(control, personalization))