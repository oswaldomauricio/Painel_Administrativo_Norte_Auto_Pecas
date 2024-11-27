import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Classes import Tabelas


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Classes import Tabelas

def MetaMes():
    metaMes = """
    SELECT 
            MF.UF,
            MF.COD_FILIAL,
            MF.DATA AS DATA_META,
            MES_META,
            VENDAS.TOTAL_VENDAS,
            MF.META,
            TRUNC(((VENDAS.TOTAL_VENDAS / MF.META) * 100),2) AS PERCENTUAL
        FROM (
            SELECT
                EMP_CODG AS COD_FILIAL,
                EXTRACT(MONTH FROM C.COMIS_EMISSAO) AS MES_META,
                EXTRACT(YEAR FROM C.COMIS_EMISSAO) AS ANO_META,     
                SUM((CASE WHEN C.COMIS_TIPO_VENDA = 'DE' THEN C.COMIS_VALOR_VENDA * -1 ELSE C.COMIS_VALOR_VENDA END)) AS TOTAL_VENDAS
            FROM velit.COMISSAO C
            WHERE TRUNC(C.COMIS_EMISSAO) >= TO_DATE('01/01/2024', 'DD/MM/YYYY')
            GROUP BY EMP_CODG, EXTRACT(MONTH FROM C.COMIS_EMISSAO), EXTRACT(YEAR FROM C.COMIS_EMISSAO)
        ) VENDAS
        LEFT JOIN ANALYTICS.METAS_FILIAIS MF ON VENDAS.COD_FILIAL = MF.COD_FILIAL AND VENDAS.MES_META = MF.MES AND VENDAS.ANO_META = MF.ANO_META
        WHERE VENDAS.COD_FILIAL = 101 and MF.DATA = TO_DATE('01/11/2024', 'DD/MM/YYYY')
        order by MF.COD_FILIAL, MES_META
"""

    tabela = Tabelas(metaMes)
    dados = tabela.execute_query()

    return dados

MetaMes()