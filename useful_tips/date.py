# useful techniques for handling dates in dataframe in python
# this script will be constantly updated for "date" challenges that we may always face and offer multiple alternative solutions

# datetime package is a useful tool to handle operations for dates in dataframe
import pandas as pd
import datetime
from datetime import timedelta
df = pd.read_csv("date.csv")

# create a new column such that we have end date + 1 
## we have a different date format in the csv so we need to use pd.to_datetime for conversion
## timedelta is a useful function in datetime for doing date calculations
df["new_end_date"] = pd.to_datetime(df.end) + timedelta(days=1)

print(df)

# next, we want to create a new column for difference between new end date and start date 
## default differnce would be shown in "x days" as the type of column is timedelta64[ns]
## we use dt.day to convert it into int for easier conditional operations **
df["new difference"] =  df.new_end_date - pd.to_datetime(df.start)

print(df)

df["new difference"] =  (df.new_end_date - pd.to_datetime(df.start)).dt.days

print(df)