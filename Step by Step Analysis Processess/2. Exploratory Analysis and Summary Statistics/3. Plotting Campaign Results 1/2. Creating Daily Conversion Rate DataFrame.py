# Import pandas into the environment
import pandas as pd

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv')
marketing.drop(marketing.index[0])
#print(marketing)

# Group by date_served and count unique users
total = marketing.groupby(['date_served'])['user_id'].nunique()
#print(total)


# Group by date_served and calculate subscribers
subscribers = marketing[marketing['converted'] == True].groupby(['date_served'])\
                         ['user_id'].nunique()
#print(subscribers)

# Calculate the conversion rate for all languages
daily_conversion_rate = subscribers / total
print(daily_conversion_rate)