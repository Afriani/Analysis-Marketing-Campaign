# Import pandas into the environment
import pandas as pd

# Import Numpy
import numpy as np

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv', parse_dates =['date_served', 'date_subscribed', 'date_canceled'])
#print(marketing)

# Subset the DataFrame
email = marketing[marketing['marketing_channel']=='Email']

# Group the email DataFrame by variant 
alloc = email.groupby(['variant'])['user_id'].nunique()

# Group marketing by user_id and variant
subscribers = email.groupby(['user_id', 
                             'variant'])['converted'].max()
subscribers_df = pd.DataFrame(subscribers.unstack(level=1)) 

# Drop missing values from the control column
control = subscribers_df['control'].dropna()

# Drop missing values from the personalization column
personalization = subscribers_df[
    'personalization'].dropna()

print('Control conversion rate:', np.mean(control))
print('Personalization conversion rate:', np.mean(personalization))