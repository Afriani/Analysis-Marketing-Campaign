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

# Reset index to turn the results into a DataFrame
daily_conversion_rate = pd.DataFrame(daily_conversion_rate.reset_index(0))

# Rename columns
daily_conversion_rate.columns = ['date_served', 'conversion_rate']

print(daily_conversion_rate)