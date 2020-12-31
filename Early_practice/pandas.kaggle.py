import pandas as pd
# https://www.kaggle.com/kashnitsky/a1-demo-pandas-and-uci-adult-dataset/notebook
name_lst = ['age', 'workclass',	'fnlwgt', 'education', 'education-num',	'marital-status', 'occupation', 'relationship',
            'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
df = pd.read_csv('adult.csv', names=name_lst)
print('1. How many men and women (sex feature) are represented in this dataset?')
print(df['sex'].value_counts())
print('Total:', df['sex'].count())

print('2. What is the average age (age feature) of women?')
print(round(df[df['sex'] == ' Female']['age'].mean(), 2))

print('3. What is the percentage of German citizens (native-country feature)?')
print(round(len(df[df['native-country'] == ' Germany'])/df.shape[0]*100, 2), '%')

print('4. What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature)?')
print('Mean:', round(df[df['salary'] == ' >50K']['age'].mean(), 2),
      'St.Deviation:', round(df[df['salary'] == ' >50K']['age'].std(), 2))

print('5. What are the mean and standard deviation of age for those who earn less than 50K per year?')
print('Mean:', round(df[df['salary'] == ' <=50K']['age'].mean(), 2),
      'St.Deviation:', round(df[df['salary'] == ' <=50K']['age'].std(), 2))

print('6. Is it true that people who earn more than 50K have at least high school education? '
      '(education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)')
edu_list = [' Bachelors', ' Prof-school', ' Assoc-acdm', ' Assoc-voc', ' Masters', ' Doctorate']
more_than50k = df[df['salary'] == ' >50K']
print(more_than50k.shape[0]-len(more_than50k[more_than50k['education'].isin(edu_list)]) == 0)

print('7. Display statistics of age for each race (race feature) and each gender. Use groupby() and describe().'
      'Find the maximum age of men of Amer-Indian-Eskimo race.')
for (race, sex), df0 in df.groupby(['race', 'sex']):
    print("Race: {}, sex: {}".format(race, sex))
    print(df0['age'].describe())
print('The maximum age of men of Amer-Indian-Eskimo race', df[df['race'] == ' Amer-Indian-Eskimo']['age'].max())

print('8. Among whom is the proportion of those who earn a lot (>50K) greater: married or single men '
      '(marital-status feature)? Consider as married those who have a marital-status starting with Married '
      '(Married-civ-spouse, Married-spouse-absent or Married-AF-spouse), the rest are considered bachelors. *')
m5k = more_than50k[more_than50k['sex'] == ' Male']                         # men with salary more than 50k
if len(m5k[m5k['marital-status'] == ' Married-civ-spouse']) > len(m5k[m5k['marital-status'] != ' Married-civ-spouse']):
    print('Among married')
else:
    print('Among single')

print('9. What is the maximum number of hours a person works per week (hours-per-week feature)? How many people work '
      'such a number of hours, and what is the percentage of those who earn a lot (>50K) among them? *')
max_w_h = df['hours-per-week'].max()
hard_workers = df[df['hours-per-week'] == max_w_h]
pr_form = '{} hours/week, {} people, {}% are rich'
print(pr_form.format(max_w_h,
                     hard_workers.shape[0],
                     round(hard_workers[hard_workers['salary'] == ' >50K'].shape[0] / hard_workers.shape[0]*100, 1)))

print('10. Count the average time of work (hours-per-week) for those who earn a little and a lot (salary) for each '
      'country (native-country). What will these be for Japan? *')
for (country, salary), df0 in df.groupby(['native-country', 'salary']):
    print(country, salary, round(df0['hours-per-week'].mean(), 2))
print('--------')
jpc = df[df['native-country'] == ' Japan']
lot = jpc.loc[jpc['salary'] == ' >50K', 'hours-per-week'].mean()
ltl = jpc.loc[jpc['salary'] != ' >50K', 'hours-per-week'].mean()
print('Japan:', round(lot, 1), ' &', round(ltl, 1))
