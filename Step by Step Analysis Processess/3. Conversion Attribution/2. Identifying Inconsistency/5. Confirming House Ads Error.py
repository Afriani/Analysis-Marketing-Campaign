# Import pandas into the environment
import pandas as pd

# Import Matplotlib
import matplotlib.pyplot as plt

# Import Numpy
import numpy as np

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv')

# Isolate the rows where marketing channel is House Ads
house_ads = marketing[marketing['marketing_channel'] == 'House Ads']

# Add the new column is_correct_lang
house_ads['is_correct_lang'] = np.where(house_ads['language_displayed'] == house_ads['language_preferred'],\
    'Yes', 'No')

# Groupby date_served and correct_language
language_check = house_ads.groupby(['date_served', 'is_correct_lang'])['user_id'].count()

# Unstack language_check and fill missing values with 0's
language_check_df = pd.DataFrame(language_check.unstack(level=1)).fillna(0)

# Divide the count where language is correct by the row sum
language_check_df['pct'] = language_check_df['Yes']/language_check_df.sum(axis=1)

# Plot and show your results
plt.plot(language_check_df.index.values, language_check_df['pct'])
plt.title('Confirming House Ads Error')
plt.show()