import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('final_merge.csv', encoding='utf8')

sentiment = data['sentiment'].tolist()

pos = sentiment.count('Pos')
neg = sentiment.count('Neg')
mix = sentiment.count('Mix')
nuet = sentiment.count('Nuet')

data = [['Mix', 'Mix', mix ], ['Neg', 'Neg', neg], ['Nuet','Nuet', nuet], ['Pos','Pos', pos]]
data = pd.DataFrame(data, columns = ['Object', 'Type', 'Value'])


colors = {'Mix':'red', 'Neg':'green', 'Pos':'blue', 'Nuet':'orange'}
c = data['Type'].apply(lambda x: colors[x])


ax = plt.subplot(111) #specify a subplot

bars = ax.bar(data['Object'], data['Value'], color=c) #Plot data on subplot axis

for i, j in colors.items(): #Loop over color dictionary
    ax.bar(data['Object'], data['Value'],width=0,color=j,label=i) #Plot invisible bar graph but have the legends specified

ax.legend()

plt.show()