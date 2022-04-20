import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rcParams['figure.figsize'] = [11, 7]
Data = pd.read_csv(r'C:\Users\hp\Desktop\covid\the_office_series.csv')

cols= []
for ind, row in Data.iterrows():
    if row['scaled_ratings'] < 0.25:
        cols.append('red')
    elif row['scaled_ratings'] < 0.5:
        cols.append('orange')
    elif row['scaled_ratings'] < 0.75:
        cols.append('lightgreen')
    else:
        cols.append('darkgreen')
cols

sizes = []
for ind, row in Data.iterrows():
    if row['has_guests'] == True:
        sizes.append(250)
    else:
        sizes.append(25)

sizes

fig= plt.figure()
plt.scatter(x= Data['episode_number'], y=Data['Viewership'], c=cols, s=sizes)
plt.title('Popularity, Quality, and Guest Appearances on the Office')
plt.xlabel("Episode Number", fontsize=18)
plt.ylabel("Viewership (Millions)", fontsize=18)


plt.show()




