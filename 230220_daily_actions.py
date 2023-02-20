

print(1+1)

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("230220_daily_actions.csv")
print(df.columns)

feeds_df = df[df['type'] == 'bottle']
sleep_df = df[df['type'] == 'sleeping']

datetime.datetime.fromtimestamp(1672070966412/1000)

feeds_df['day'] = feeds_df.apply(lambda row: datetime.datetime.fromtimestamp(row['start_millis']/1000).day, axis=1)
feeds_df['month'] = feeds_df.apply(lambda row: datetime.datetime.fromtimestamp(row['start_millis']/1000).month, axis=1)
feeds_df['hour'] = feeds_df.apply(lambda row: datetime.datetime.fromtimestamp(row['start_millis']/1000).hour, axis=1)
feeds_df['minute'] = feeds_df.apply(lambda row: datetime.datetime.fromtimestamp(row['start_millis']/1000).minute, axis=1)


feeds_time_df = feeds_df[['volume', 'day', 'month', 'hour', 'minute']]

feeds_time_df.hist('volume')

plt.savefig('plot.png')

