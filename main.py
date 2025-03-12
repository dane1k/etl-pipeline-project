import pandas as pd

data = { 'Name' : ['Danya', 'Vishwa', 'Filip'],
        'Age': [20, 21, 22],
        'City': ['Auckland', 'Auckland', 'Auckland']}

df = pd.DataFrame(data)

print(df)