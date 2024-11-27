import mysql.connector
from dotenv import load_dotenv
import os
import warnings
import pandas as pd

warnings.filterwarnings('ignore')

class ConnectToDB:
    def __init__(self):
        # Carregar variáveis de ambiente do arquivo .env
        load_dotenv()

        # Carregar configurações do banco de dados a partir do .env
        self.host = os.getenv("SERVERMYSQL")
        self.database = os.getenv("DATABASEMYSQL")
        self.user = os.getenv("USERNAMEMYSQL")
        self.password = os.getenv("PASSWORDMYSQL")

        # Validar se as variáveis de ambiente estão carregadas
        if not all([self.host, self.database, self.user, self.password]):
            raise ValueError("Variáveis de ambiente para conexão ao banco de dados não foram definidas corretamente.")

        # Inicializar a conexão
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor(dictionary=True)
            
            print("Conectado ao banco de dados com sucesso!")
        except mysql.connector.Error as err:
            raise ConnectionError(f"Erro ao conectar ao banco de dados: {err}")


if __name__ == "__main__":
    db = ConnectToDB()