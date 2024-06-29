import pandas as pd
df = pd.read_csv('GoogleApps.csv')

df.info()
print(df.describe())
# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
paid = df[df['Type']=='Paid']
print(paid['Price'].min())

# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
art = df[df['Category']=='ART_AND_DESIGN']
print(art['Installs'].median())

# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
paid = df[df['Type']=='Paid']
free = df[df['Type']=='Free']
result = free['Reviews'].max() - paid['Reviews'].max()
print(result)
# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?


# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?


# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
