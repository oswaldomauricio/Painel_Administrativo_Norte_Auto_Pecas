import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Classes import Tabelas

query = """
    SELECT n.emp_codg,
                n.nnfc_chave_nfe AS CHAVE,
                n.nnfc_serie,
                n.nnfc_numero,
                n.nnfc_cnpj_emitente,
                n.nnfc_razao_social,
                n.nnfc_data_emissao,
                n.nnfc_valor_total,
                n.nnfc_situacao_nfe,
                n.nnfc_status_manif,
                '' as nnfc_xml, /*extract(n.nnfc_xml,'/').getClobVal()*/
                n.nnfc_nsu,
                decode(
                        EXISTSNODE(n.nnfc_xml, '/nfeProc/NFe', 'xmlns=http://www.portalfiscal.inf.br/nfe'),
                        1, 'SIM',
                        0, 'NAO')as Download_Disponivel,
                ''||n.nnfc_num_protocolo as nnfc_num_protocolo
        from nfex_nf_consulta n
        where   n.nnfc_status_manif in ('PEN', 'CIE') AND n.emp_codg = 101
        and nvl(n.nnfc_tipo,'NFE') = 'NFE'
        and n.nnfc_data_emissao >= TO_DATE('01/01/2024', 'DD/MM/YYYY')
        order by n.nnfc_data_emissao desc, n.nnfc_numero desc , n.nnfc_serie
"""

tabela = Tabelas(query)
dados = tabela.execute_query()

print(dados)
