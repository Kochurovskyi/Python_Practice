import pandas as pd
import time as time
tm_start = time.time()

dt = pd.read_csv('run.csv')
sr = pd.Series(dt['Distance'].values, pd.to_datetime(dt['Date'].values))                # Series of Date/Distance
print('1. General info (statistics):')
print(round(sr.describe(), 2))
print('2. Longest 5 runnings:')
print(sr.sort_values()[-5:])
print('3. The list of Marathons & Half-Marathons:')
print(sr[sr.isin(['21.1', '42.2'])])
print('4. 90% percentile:', sr.quantile(.9))
print('5. Sums & mean yearly:')
for i in sr.index.year.unique():
    print(i, 'year ->', round(sr.loc[str(i)].sum(), 2), 'km .... ->', round(sr.loc[str(i)].mean(), 2), 'km')
print('6. The longest runnings -', sr[sr.between(30, 100)].count(), 'ruunings between 30 & 100:')
print(sr[sr.between(30, 100)])
print('7. The most frequent distances:')
print(sr.value_counts()[:5])

print('8. HR mean yearly:')
sr = pd.Series(dt['Avg HR'].values, pd.to_datetime(dt['Date'].values))                # Series of Date/Distance
for i in sr.index.year.unique():
    print(i, 'year ->', round(sr.loc[str(i)].mean(), 2), 'hpm')
print(round((time.time()-tm_start), 3))
