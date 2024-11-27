import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.dataBase_ORACLE import get_connection

class Tabelas:
    def __init__(self, query):
        self.query = query  

    def execute_query(self):
        conn = get_connection()
        
        dados = pd.read_sql(self.query, conn)

        conn.close()

        return dados
    
