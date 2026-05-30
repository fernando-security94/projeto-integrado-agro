# exemplo de captura e leitura de dados tipo json com API
# usando pandas. Normalmente, quando se extrai dados de API
# são dados em tempo real
# DATAVIZ com pandas precisa ser acompanhada de matplotlib.pyplot

import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=10/04/2015&dataFinal=10/04/2025")
print(df_selic.info())



# verificar se há dados duplicados
# keep='last' mantem o ultimo registro em caso de duplicidade
# inplace=True faz com que a alteração seja salva no df
df_selic.drop_duplicates(keep='last', inplace=True)

# adicionando a data da extração com date.today e 
# adicionando colunas e valores
data_extracao = date.today()
df_selic['Data de extração'] = data_extracao
df_selic['Responsável'] = "Fernando Ribeiro"


print(df_selic.info())
print("Taxa selic ao longo de 10 anos:\n")
print(df_selic.head(20))

#print(df_selic)

# usando funcao loc[] para localizar valores
# a funcao loc[] busca os valores através dos indices
# podendo ser chamada com um ou multiplos valores

localiza_valor = df_selic.loc[1]
localiza_valores = df_selic.loc[[10, 20, 50, 70]]  #add lista como parametro em loc
utimo_valor = df_selic.loc[2509]

print(f'\nValor localizado nos índices 10, 20, 50 e 70:\n {localiza_valores}\n')
print(f'Último valor: {utimo_valor}\n')
print('-' * 90)


# teste de buscar valor com base em uma condicao
teste = df_selic['valor'] < 0.05 
print(type(teste))
print(teste)
print('-' * 90)


# buscar datas com taxa selic a baixo de 10%
taxa_menor_cinco = df_selic['valor'] < 0.05
print(taxa_menor_cinco.head(10))

# filtrando o dataframe para exibir o valor 
# a partir do teste booleano
taxas_filtradas = df_selic[df_selic['valor'] < 0.05]

# exibir os resultados add o parametro 'data'
print("\nDatas em que a taxa Selic esteve abaixo de 5%:\n")
print(taxas_filtradas[['data', 'valor']].head(20))

# garantindo que a coluna data seja do tipio datetime
# dayfirst=True garante que o compilador entenda o formato da data
df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)

# filtrar as taxas abaixo de 5%
filtro_grafico = df_selic['valor'] < 0.05
taxas_baixas = df_selic[filtro_grafico]

# plotando todas as taxas 
plt.figure(figsize=(12, 6))
plt.plot(df_selic['data'], df_selic['valor'], label='Taxa Selic', color='royalblue')

# destacar onde a taxa foi < 5%
plt.scatter(taxas_baixas['data'], taxas_baixas['valor'], color='red', label='Taxas < 5%', zorder=5)

# formatar o eixo X para exibir mes/ano
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b/%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())

# melhorar legibilidade do eixo x
plt.xticks(rotation=45)

# personalizacao do grafico
plt.title("Taxa Selic com Destaque para Valores abaixo de 5%")
plt.xlabel('Data')
plt.ylabel('Valor da Taxa selic')
plt.axhline(0.05, color='gray', linestyle='--', linewidth=1, label='Limite de 5%')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# salvar em csv para criar dashboard no Tableau
df_selic.to_csv('selic_dados.csv', index=False)



'''
Foi necessario especificar a data para conseguir recuperar os dados da API,
tendo um limite de 10 anos!

https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=10/04/2015&dataFinal=10/04/2025

'''
