import sys
import os
import warnings
from dotenv import load_dotenv

warnings.filterwarnings('ignore')

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cx_Oracle

def get_connection():
    # retornará a conexão com o banco de dados.
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient_11_2")
    except cx_Oracle.ProgrammingError:
        pass  # Ignorar se o cliente já foi inicializado
    load_dotenv()

    SERVERORACLE = os.getenv("SERVERORACLE")
    PORTAORACLE = os.getenv("PORTAORACLE")
    SERVICENAMEORACLE = os.getenv("SERVICENAMEORACLE")
    PASSWORDORACLE = os.getenv("PASSWORDORACLE")
    USERNAMEORACLE = os.getenv("USERNAMEORACLE")

    # Configuração de conexão
    username = USERNAMEORACLE
    password = PASSWORDORACLE
    dsn = cx_Oracle.makedsn(SERVERORACLE, PORTAORACLE, service_name=SERVICENAMEORACLE)

    try:
        conn = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        # print("Conexão bem-sucedida!")
        return conn
    except cx_Oracle.DatabaseError as e:
        print("Erro ao conectar ao banco de dados:", e)
        raise
