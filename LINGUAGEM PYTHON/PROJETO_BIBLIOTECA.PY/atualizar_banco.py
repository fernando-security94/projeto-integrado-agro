import sqlite3

def adicionar_coluna_estoque():
    conexao = sqlite3.connect("biblioteca.db")  # ou "data/biblioteca.db" se estiver nessa pasta
    cursor = conexao.cursor()
    
    try:
        cursor.execute("ALTER TABLE livros ADD COLUMN estoque INTEGER DEFAULT 0")
        print("Coluna 'estoque' adicionada com sucesso!")
    except sqlite3.OperationalError as e:
        print(f"Aviso: {e} (A coluna já pode ter sido criada anteriormente)")
    
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    adicionar_coluna_estoque()
