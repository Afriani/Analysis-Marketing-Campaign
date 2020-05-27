# Import pandas into the environment
import pandas as pd

# Import numpy
import numpy as np

# Import marketing.csv 
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/PYTHON/Analyzing Marketing Campaigns with Pandas/DATA/Marketing2.csv', parse_dates =['date_served', 'date_subscribed', 'date_canceled'])

# Mapping for channels
channel_dict = {"House Ads": 1, "Instagram": 2, 
                "Facebook": 3, "Email": 4, "Push": 5}

# Map the channel to a channel code
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# Mapping for channels
channel_dict = {"House Ads": 1, "Instagram": 2, 
                "Facebook": 3, "Email": 4, "Push": 5}

# Map the channel to a channel code
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# Add the new column is_correct_lang
marketing['is_correct_lang'] = np.where(
    marketing['language_preferred'] == marketing['language_displayed'], 
    'Yes', 
    'No'
)

# Add a DoW column
marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek

print(marketing.info())