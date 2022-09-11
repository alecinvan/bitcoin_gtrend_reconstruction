
from datetime import date, timedelta
import pandas as pd
import numpy as np
import scipy as sp
import os
#import matplotlib.pyplot as plt



path = os.getcwd()
print(path)

# Read the downloaded data files into dfs
df_monthly = pd.read_csv(path + '/' + 'monthly.csv', index_col='date')
df_weekly = pd.read_csv(path + '/' + 'weekly.csv',index_col='date')
df_hourly = pd.read_csv(path + '/' + 'hourly.csv',index_col='date')

# To easy to manipulate, I drop the time columns for each dataset
df_weekly = df_weekly.drop(columns=['time_week'])
df_monthly = df_monthly.drop(columns=['time_month'])
df_hourly = df_hourly.drop(columns=['time_hour'])


def merge_rescale_data(df1, df2, df1_col, df2_col, scale, newcol)->pd.DataFrame:
    # Merge monthly/weekly data to weekly/hourly data 
    assemble_df = df1.join(df2)
    # Replace NaNs with values
    assemble_df[df2_col].ffill(inplace=True)
    # Scale weekly/hourly data by valid monthly/weekly data weights
    assemble_df[scale] = assemble_df[df2_col] / 100
    assemble_df[newcol] = (assemble_df[df1_col] * assemble_df[scale]).astype(int)
    
    return assemble_df

  
# rescale the weekly data and generate the weekly consistent data
assemble_weekly = pd.DataFrame(merge_rescale_data(df_weekly, df_monthly, 'value_week', 'value_month', 'scale_measure', 'renormalized_weekly'))

# Generate valid comparable weekly data to scale global hourly data 
weekly_scale = pd.DataFrame(assemble_weekly, columns= ["renormalized_weekly"])
# Make the weekly index consistent to hourly index 
weekly_scale.index = pd.to_datetime(weekly_scale.index).strftime('%Y-%m-%d %H:%M:%S')

# rescale the hourly data and generate the hourly consistent data
assemble_hourly = pd.DataFrame(merge_rescale_data(df_hourly, weekly_scale, 'value_hour', 'renormalized_weekly', 'scale_measure', 'renormalized_hour'))
# Generate comparable hourly data from 2017 to now 
hourly_comparable = pd.DataFrame(assemble_hourly, columns= ["renormalized_hour"])

# Write into the file 
hourly_comparable.to_csv('path + '/' + 'hourly_comparable.csv')
                         
                         
                         
                         
