import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')
# Виведи інформацію про всі DataFrame, щоб дізнатися, які стовпці потребують очищення
df.info()
# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?
result = df[pd.isnull(df['Rating'])]
print(len(result))
# Заміни порожнє значення ('NaN') рейтингу ('Rating') для таких програм на -1.
df['Rating'].fillna(-1, inplace=True)

df.dropna(inplace=True)
df.info()


# Визнач, яке ще значення розміру ('Size') зберігається в датасеті крім Кілобайтів та Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.
def clean_size(size):
    if size[-1] == 'M':
        result = size[:-1]
        return float(result)
    elif size[-1]=='k':
        result = size[:-1]
        return float(result) / 1024
    else:
        return -1
    
df['Size'] = df['Size'].apply(clean_size)
df.info()

# Чому дорівнює максимальний розмір ('Size') додатків з категорії ('Category') 'TOOLS'?
tools= df[df['Category'] == 'TOOLS']
max_size = tools['Size'].max()
print(max_size)

# Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто, якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000

def clean_installs(installs):
    if installs[-1] == '+':
        result = installs[:-1].replace(',', '')
        return int(result)
    else:
        return 0

df['Installs'] = df['Installs'].apply(clean_installs)
df.info()

# Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди клітинку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї клітинки?

# У якої програми не вказаний тип ('Type')? Який тип там потрібно записати залежно від ціни?

# Виведи інформацію про все DataFrame, щоб переконатися, що очищення пройшло успішно

df = df.drop(['Unnamed: 0', 'Current Ver', 'Last Updated', 'Android Ver'], axis=1)
df.to_csv('cleaned.csv')

