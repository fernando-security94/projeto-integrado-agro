# Construção de classe para acessar banco de dados

import pandas as pd
from sqlalchemy import create_engine

class DataBase():
    def __init__(self):
        self.nome = 'mysql+pymysql ://mysql_user : mysql_password@mysql_host/mysql_db'
        self._con = create_engine(self.name)

        def query(self, query):
            df = pd.read_sql(query, con=self._con)
            return df
        
        def filmes_avaliados(self, id_cliente):
            query=f"""
            SELECT ID_USUARIO, ID_FILME, AVALIACAO, DATA FROM AVALIACOES WHERE ID_USUARIO = {id_cliente}

"""
            df = self.query(query)
            return df