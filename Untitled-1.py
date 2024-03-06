import pandas as pd

# Исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot encoding
unique_values = sorted(data['whoAmI'].unique())
one_hot_encoding = pd.DataFrame(0, columns=unique_values, index=data.index)
one_hot_encoding = one_hot_encoding.add(pd.get_dummies(data['whoAmI']), fill_value=0)

# Объединение исходного DataFrame с one hot encoding
data = pd.concat([data, one_hot_encoding], axis=1)

data.head()
