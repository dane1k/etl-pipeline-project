import pandas as pd

data = { 'Name' : ['Danya', 'Vishwa', 'Sanya', 'Filip'],
        'Age': [20, 21, 18, 22],
        'City': ['Auckland', 'Auckland', 'Auckland', 'Auckland']}

df = pd.DataFrame(data)

print(df)