import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Classes import Tabelas

def MetaSemanal():
    MetaSemanal = """
        SELECT 
            A.COD_FILIAL,
            A.UF,
            A.DATA,
            A.DATA_INICIO,
            A.DATA_FIM,
            A.META_SEMANAL,
            SUM(VENDAS.TOTAL_VENDAS) AS TOTAL_VENDAS_SEMANA,
            TRUNC(((SUM(VENDAS.TOTAL_VENDAS) / A.META_SEMANAL) * 100), 2) AS PERCENTUAL
        FROM (
            SELECT 
            MF.COD_FILIAL,
            MF.UF,
            MF.MES,
            MF.GERENTE,
            MF.ANO_META,
            MF.DATA,
            MS.DATA_INICIO,
            MS.DATA_FIM,
            TRUNC(((MF.META / MD.QTD_DIAS) * MS.QTD_DIAS),2) AS META_SEMANAL  ---- DIMINUI O CALCULO DAS METAS SEMANAIS
        FROM ANALYTICS.METAS_FILIAIS MF
        LEFT JOIN ANALYTICS.PARAMETRO_META_SEMANA MS ON MF.DATA = MS.DATA
        LEFT JOIN ANALYTICS.PARAMETRO_META_DIAS MD ON MD.DATA = MF.DATA  ---- INCLUI ESSE LEFT JOIN PARA PEGAR AUTOMATICO A QUANTIDADE DE DIAS DO MES
        ) A
        LEFT JOIN (
            SELECT
                C.EMP_CODG AS COD_FILIAL,
                TRUNC(C.COMIS_EMISSAO) AS DATA,
                (CASE WHEN C.COMIS_TIPO_VENDA = 'DE' THEN C.COMIS_VALOR_VENDA * -1 ELSE C.COMIS_VALOR_VENDA END) AS TOTAL_VENDAS
            FROM VELIT.COMISSAO C
            WHERE TRUNC(C.COMIS_EMISSAO) >= TO_DATE('01/01/2024', 'DD/MM/YYYY')
        ) VENDAS
        ON VENDAS.DATA BETWEEN A.DATA_INICIO AND A.DATA_FIM AND A.COD_FILIAL = VENDAS.COD_FILIAL
        WHERE A.DATA = TO_DATE('01/11/2024', 'DD/MM/YYYY') -- Definir o mês
        AND A.COD_FILIAL = 101 -- Definir a loja
        GROUP BY
            A.COD_FILIAL,
            A.UF,
            A.DATA,
            A.DATA_INICIO,
            A.DATA_FIM,
            A.META_SEMANAL
        ORDER BY  
            A.COD_FILIAL, A.DATA, A.DATA_INICIO
"""

    tabela = Tabelas(MetaSemanal)
    dados = tabela.execute_query()

    return dados

MetaSemanal()