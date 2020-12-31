# https://www.w3resource.com/python-exercises/pandas/practice-set1/index.php
import pandas as pd

dfd = pd.read_csv('diamonds.csv')
print(dfd.info())                                                       # 0. general info
im_cols = ['carat', 'cut', 'x', 'y', 'z']                               # 1. only a couple most important columns
print('-----------')
print(dfd[im_cols].head())
dfd['Quality-Color'] = dfd.cut + '-' + dfd.color                        # 2. Columns concatenate into 'Quality-Color'
# dfd.drop('cut', axis=1, inplace=True)                                 # 3. Deleting the column 'cut'
dfd = dfd.rename(columns={'color': 'diam_color',                        # 4. Renaming a couple of columns
                          'clarity': 'diam_clarity'})
print('----------')
print(dfd.head())
print('----------')
# dfd.drop(['x', 'y', 'z'], axis=1, inplace=True)                       # 5. Deleting three columns at once
drop_indices = dfd[(dfd.x == 0) | (dfd.y == 0) | (dfd.z == 0)].index    # 8. The list of indices where size is 0
dfd.drop(drop_indices, axis=0, inplace=True)                            # 7. Removing rows where x,y,z = 0
cut_sort = dfd.sort_values(by='cut', ascending=True)                    # 8. Sorting by 'cut'
price_sort = dfd.price.sort_values(ascending=True)                      # 9. Soring by 'price', returns only Series
print(dfd[dfd['carat'] > 0.3])                                          # 10. 'carat' filter -> more than 0.3
print('----------')
# print(dfd.mean())                                                     # 11. mean data of all numeric columns
dfd['all_mean'] = dfd.mean(axis=1)                                      # 12. mean data of all rows
dfd['size_mean'] = dfd[['x', 'y', 'z']].mean(axis=1)                    # 13. size mean in additional column
print(dfd.groupby('cut')['price'].mean())                               # 14. mean data per each 'cut'
print('----------')
print(dfd.cut.value_counts())                                           # 15. the quantity of each 'cut'
print('----------')
print(dfd.carat.describe())                                             # 16. All stats for 'carat'
dfd = dfd.set_index('diam_color')                                       # 17. 'color as Index
print('----------')
dfd.index.name = 'diam_color'                                           # 18. Index reset
dfd.reset_index(inplace=True)
print(dfd.iloc[0, :])                                                    # 19. Only the first row
print('----------')
print(dfd.iloc[0:5, 2:5])                                                # 20. Slicing (iloc)
print('----------')
print(dfd.loc[0:5, ['carat', 'x', 'y', 'z']])                            # 20. Slicing (loc)
print('----------')
print(dfd[dfd['cut'] == 'Premium'].diam_color.head())                   # 21. Only color of 'Premium' size (cut)
print('----------')
print(dfd.diam_clarity.duplicated().sum())                              # 22. Duplicated rows
