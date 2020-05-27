# Import pandas into the environment
import pandas as pd

# Import Matplotlib
import matplotlib.pyplot as plt

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/Analyzing Marketing Campaigns with Pandas/DATA/marketing2.csv')

# Count the subs by subscribing channel and day
retention_total = marketing.groupby(['date_subscribed','subscribing_channel'])\
                                    ['user_id'].nunique()

# Print results
print(retention_total.head())

# Count the retained subs by subscribing channel and date subscribed
retention_subs = marketing[marketing['is_retained'] == True]\
                           .groupby(['date_subscribed','subscribing_channel'])\
                            ['user_id'].nunique()

# Divide retained subscribers by total subscribers
retention_rate = retention_subs / retention_total
retention_rate_df = pd.DataFrame(retention_rate.unstack(level=1))

# Plot retention rate
retention_rate_df.plot()

# Add a title, x-label, y-label, legend and display the plot
plt.title('Retention Rate by Subscribing Channel')
plt.xlabel('Date Subscribed')
plt.ylabel('Retention Rate (%)')
plt.legend(loc = 'upper right', labels = retention_rate_df.columns.values)
plt.show()