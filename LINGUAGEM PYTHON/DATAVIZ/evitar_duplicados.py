# # Verificar se a tabela já tem dados
# cursor.execute('SELECT COUNT(*) FROM vendas1')
# quantidade = cursor.fetchone()[0]

# if quantidade == 0:
#     # Se não tiver dados, insere
#     cursor.executemany('''
#     INSERT INTO vendas1(data_venda, produto, categoria, valor_venda)
#     VALUES (?, ?, ?, ?)
#     ''', vendas)
#     conn.commit()
#     print('Dados inseridos com sucesso!')
# else:
#     print('Tabela já possui dados. Nenhuma inserção realizada.')
