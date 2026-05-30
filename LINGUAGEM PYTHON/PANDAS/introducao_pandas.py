# exemplo de criacao de Series a partir de uma lista
# com Pandas

import pandas as pd

data = [10, 20, 30, 40, 50]
series1 = pd.Series(data)
print("Series atraves da lista data:")
print(series1)

print(f'Lista data: {data}')

print('#############\n')

# criando Series a partir de um dict
data2 = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
series2 = pd.Series(data2)
print("Series atraves do dict data2:")
print(series2)
print(f'Dicionario data2: {data2}')

print('#############\n')
