# Import pandas into the environment
import pandas as pd

# Import plot
import matplotlib.pyplot as plt

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv', parse_dates =['date_served', 'date_subscribed', 'date_canceled'])
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
daily_conversion_rate.columns = ['date_subscribed', 'conversion_rate']

# Create a line chart using daily_conversion_rate
daily_conversion_rate.plot('date_subscribed', 'conversion_rate')

plt.title('Daily conversion rate\n', size = 16)
plt.ylabel('Conversion rate (%)', size = 14)
plt.xlabel('Date', size = 14)

# Set the y-axis to begin at 0
plt.ylim(0)

# Display the plot
plt.show()