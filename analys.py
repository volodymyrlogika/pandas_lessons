import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')
# df['Size'].plot(kind = 'hist')
# df[df['Type'] == 'Paid']['Price'].plot(kind = 'box')

df.plot(x='Rating', y = 'Installs', kind='scatter')
# df['Category'].value_counts().plot(kind='pie')
df['Category'].value_counts().nlargest(10).plot(kind='pie', figsize=(8,5), grid=True)
plt.show()