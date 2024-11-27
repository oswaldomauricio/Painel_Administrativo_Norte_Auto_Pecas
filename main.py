import sys
import os
import pandas as pd



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Tables.Classes.Classes import Tabelas

from services.dataBase_ORACLE import get_connection #dados de conexão do BD
from Tables.f_manifesto import MANIFESTO #TABELA FATO
from Tables.f_notas_de_entrada import NOTAS_DE_ENTRADA #TABELA FATO
from Tables.f_metasMes_Loja import MetaMes
from Tables.f_metasSemanal_Loja import MetaSemanal


def main():
    # f_notasEntrada = NOTAS_DE_ENTRADA()
    # f_manifesto = MANIFESTO()

    # chave_Merge = pd.merge(f_notasEntrada, f_manifesto, on="CHAVE", how="outer")
    
    # Tabelarow10 = chave_Merge.loc[0:10000]

    # return Tabelarow10

    df_metaMes = MetaMes()
    df_metaSemanal = MetaSemanal()

    return df_metaMes, df_metaSemanal
    