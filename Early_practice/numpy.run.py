import numpy as np
import pandas as pd

# TODO header to each result to be added

data = np.genfromtxt('run.csv', dtype='str', delimiter=',', skip_header=1)

# Data preparation:
distances = np.array(data[:, 2], dtype=float)                                           # the array of distances
running_dates = np.array(pd.to_datetime(data[:, 0])).astype('datetime64')               # the array of dates (pd)
vo = np.array(data[:, 6], dtype=int)                                                    # the array of Vo2Max
r_time = np.array(pd.to_timedelta(data[:, 3])).astype('timedelta64[s]').astype(int)     # running-time in seconds (pd)
speed = np.array(distances / r_time*3600, dtype=float)                                  # the array of speed

# Morning runnings
print('Calculating morning runnings')
running_start_hour = running_dates.astype('datetime64[h]')
midnight = running_dates.astype('datetime64[D]')
hours = (np.array(running_start_hour-midnight)).astype(int)
print('Total morning runnings (started till 7am):{} out of {} ({}%)'
      .format(len(data[hours < 7]), len(running_dates), round(np.mean(hours < 7)*100, 1)))
# print('Third quartile:', np.percentile(hours, 75))
print('------- runnings itself:')
print(data[hours < 7])
print('Press ENTER to proceed...')
input()

# Some statistics & Sorting (Running times & HR)
print('5 longest(timely) runnings)')
print(data[np.argsort(r_time)][-5:])                                           # 5 longest(timely) runnings
print('5 fastest runnings)')
print(data[np.argsort(speed)][-5:])                                            # 5 fastest runnings
print('5 runnings withe the highest HR(max) (more than 200hrm')
print(data[np.argsort(data[:, 5])][-5:])                                       # 5 runnings withe the highest HR(max)
print('Press ENTER to proceed...')
input()

# Again some statistics & Sorting (Distances)
print('Some statistics and sorting:')
print('Average distance', round(np.mean(distances), 1))                 # Average distance
print('Distance median', round(np.median(distances), 1))                # Distance median
print('Standard deviation', round(np.std(distances), 1))                # Standard deviation
print('Sum', round(np.sum(distances), 1))                               # Sum
print('Distance percentage longer 20k:', round((np.mean(distances > 20)*100), 1), '%')
print('Third quartile (daytime - when I made 3/4 my runnings):', np.percentile(hours, 75))
print('Runnings longer than 300% of median:')
print(data[distances/np.mean(distances) > 3])
print('20 longest runnings:')
print(data[np.argsort(np.asarray(data[:, 2], dtype=float))][-20:, :])     # Sorted by distance (column #2)
print('Press ENTER to proceed...')
input()

# runnings sums as per weekday
print("Running sum as per each weekday:")
weekday_list = np.array(['sun:', 'mon:', 'tue:', 'wed:', 'thu:', 'fri:', 'sat:'])
week_days = (running_dates.astype('datetime64[D]').view('int64')-3) % 7
week_day_sums = np.bincount(week_days.astype('int32'), weights=distances).astype('float32')
print(np.column_stack((weekday_list, week_day_sums)))
print('Press ENTER to proceed...')
input()

# looking for 20 longest running breaks
print('20 most long breaks between runnings:')
break_list = np.diff(running_dates.astype('datetime64[D]'))
break_arg_sort = np.argsort(break_list)[-10:]                                               # the biggest 10 breaks
lst = break_list[break_arg_sort].reshape(10, 1).astype('str')
start = data[break_arg_sort]
end = data[break_arg_sort+1]
args = (lst, np.full((10, 1), 'Break start:'), start, np.full((10, 1), 'Break end:'), end)
breaks = np.concatenate(args, axis=1)
print(breaks)
print('Press ENTER to proceed...')
input()

# Average daily runnung analyzing each year`
print("Let's analyze average runnings per each year (year/distances(avg)/quantities):")
year_list: ndarray = np.array(running_dates, dtype='datetime64').astype('datetime64[Y]').astype('int')
np.seterr(divide='ignore', invalid='ignore')
year_avg = np.bincount(year_list, weights=distances).astype('float32') / np.bincount(year_list).astype('float32')
year_avg = year_avg[np.isfinite(year_avg)]                                                      # removing 'NaNs
yqty = np.bincount(year_list)
year_avg_qty = np.column_stack((np.unique(year_list).astype('datetime64[Y]').astype('str'),
                                year_avg.astype('str'),
                                yqty[yqty > 0].astype('str')))
print(year_avg_qty)
print('Press ENTER to proceed...')
input()

# Average daily runnung analyzing each month
print("Let's analyze average runnings per each month:")
month_list = np.array(running_dates, dtype='datetime64').astype('datetime64[M]').astype('int')
np.seterr(divide='ignore', invalid='ignore')
month_avg = np.bincount(month_list, weights=distances).astype('float32') / np.bincount(month_list).astype('float32')
month_sum = month_avg[np.isfinite(month_avg)]                                                      # removing 'NaNs
print(np.column_stack((np.unique(month_list).astype('datetime64[M]').astype('str'), month_sum.astype('str'))))
