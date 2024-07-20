import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')
# df['Size'].plot(kind='hist', bins = 15, grid = True)
# df[df['Type']=='Paid']['Price'].plot(kind='box')

# df.plot(x = 'Rating', y= 'Reviews', kind='scatter')
# paid  = df[df['Type']=='Paid']
# paid.plot(x='Price', y= 'Rating', kind='scatter')

# df['Category'].value_counts().nlargest(10).plot(kind='pie') 
df['Category'].value_counts().plot(kind='barh', grid=True, figsize=(8,5)) 
plt.show()

