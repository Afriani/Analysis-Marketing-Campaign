# Import pandas into the environment
import pandas as pd

# Import Numpy
import numpy as np

# Import Stats
from scipy import stats

# Import t-test
from scipy.stats import ttest_ind

# Import marketing.csv with date columns
marketing = pd.read_csv('C:/Users/Hp ProBook 640/Documents/PYTHON/Analyzing Marketing Campaigns with Pandas/DATA/Marketing2.csv', parse_dates =['date_served', 'date_subscribed', 'date_canceled'])
#print(marketing)


# ab_segmentation and lift formula for language_displayed
def ab_segmentation(segment):
  # Build a for loop for each subsegment in marketing
  for subsegment in np.unique( marketing['language_displayed']):    
      def lift(a,b):
           # Calcuate the mean of a and b 
              a_mean = np.mean(control)
              b_mean = np.mean(personalization)
    
           # Calculate the lift using a_mean and b_mean
              lift = (b_mean - a_mean) / a_mean
  
              return str(round(lift*100, 2)) + '%'
      # Limit marketing to email and subsegment
      email = marketing[(marketing['marketing_channel'] == 'Email') & (marketing[segment] == subsegment)]

      subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
      subscribers = pd.DataFrame(subscribers.unstack(level=1)) 
      control = subscribers['control'].dropna()
      personalization = subscribers['personalization'].dropna()

      print(subsegment)
      print('lift:', lift(control, personalization)) 
      print('t-statistic:', stats.ttest_ind(control, personalization), '\n\n')

ab_segmentation('language_displayed')


# ab_segmentation and lift formula for age_group
def ab_segmentation(segment):
  # Build a for loop for each subsegment in marketing
  for subsegment in np.unique( marketing['age_group']):    
      def lift(a,b):
           # Calcuate the mean of a and b 
              a_mean = np.mean(control)
              b_mean = np.mean(personalization)
    
           # Calculate the lift using a_mean and b_mean
              lift = (b_mean - a_mean) / a_mean
  
              return str(round(lift*100, 2)) + '%'
      # Limit marketing to email and subsegment
      email = marketing[(marketing['marketing_channel'] == 'Email') & (marketing[segment] == subsegment)]

      subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
      subscribers = pd.DataFrame(subscribers.unstack(level=1)) 
      control = subscribers['control'].dropna()
      personalization = subscribers['personalization'].dropna()

      print(subsegment)
      print('lift:', lift(control, personalization)) 
      print('t-statistic:', stats.ttest_ind(control, personalization), '\n\n')

ab_segmentation('age_group')