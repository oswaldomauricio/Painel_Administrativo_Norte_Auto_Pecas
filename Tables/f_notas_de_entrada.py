import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.dataBase_ORACLE import get_connection

def NOTAS_DE_ENTRADA():
    conn = get_connection()

    cursor = conn.cursor()

    query = """
        SELECT NT.NFE_SEQUENCIAL,
            NT.EMP_CODG,
            NT.FUNC_USUARIO AS FUNCIONARIO,
            NT.NFE_CHAVE_NF_ELETRONICA AS CHAVE,
            NT.NFE_DTA_EMISSAO_NOTA, 
            NT.NFE_DTA_ATUALIZACAO,
            NT.NFE_NUMERO_NOTA,
            NT.NFE_STATUS AS STATUS,
            NT.NFE_RAZAO_SOCIAL       
        FROM VELIT.NOTAS_DE_ENTRADA NT
        WHERE NT.NFE_DTA_EMISSAO_NOTA >= TO_DATE('01/01/2024', 'DD/MM/YYYY') 
        AND NT.NFE_CHAVE_NF_ELETRONICA IS NOT NULL
"""

    cursor.execute(query)

    dados_NotasEntrada = pd.read_sql(query, conn)

    return dados_NotasEntrada

NOTAS_DE_ENTRADA()