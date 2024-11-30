import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.dataBase_ORACLE import get_connection

class Login:
    def __init__(self,  name, password):
        self.name = name
        self.password = password

    def execute_query(self):
        conn = get_connection()
        
        dados = pd.read_sql("""
            SELECT * FROM ANALYTICS.USERS U 
            WHERE NAME = :name AND PASSWORD = :password
        """, conn, params={"name": self.name, "password": self.password})

        conn.close()

        return dados
    
    

# login = Login(name="oswaldo", password="44844")
# dados = login.execute_query()

# print(dados)
