import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from streamlit_cookies_controller import CookieController
import pandas as pd

# Função de logout
def logout_user():
    controller.remove('user_status')
    controller.remove('username')
    controller.remove('password')
    controller.remove('user_id')

# Inicializa o controlador de cookies
controller = CookieController()

# Obtém os cookies atuais
cookies = controller.getAll()
st.write("Cookies atuais:", cookies)

# Verifica se o usuário está logado
if cookies.get('user_id'):
    st.write("Usuário logado:", cookies.get('user_id'))
    with st.sidebar:
        if st.button("Sair"):
            logout_user()  # Agora a função está definida antes