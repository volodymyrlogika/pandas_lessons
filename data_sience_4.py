import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')
# df["Size"].plot(kind='box')

df.plot(x='Rating', y='Installs', kind='scatter')

plt.show()
