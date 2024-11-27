import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controllers.LoginController import Login

login_query = """
            SELECT * FROM ANALYTICS.USERS U 
            WHERE NAME = :name AND PASSWORD = :password
        """
st.image('../Images/Logo.png')



# st.title('Página de Login')

username = st.text_input('Usuário', value='', placeholder='Digite seu nome de usuário')
password = st.text_input('Senha', value='', placeholder='Digite sua senha', type='password')

if st.button('Entrar'):
    if username and password:
        login_user = Login(login_query, name=username, password=password)
        try:
            dados = login_user.execute_query()
            if not dados.empty:
                st.success(f'Bem-vindo(a), {username}!')
                st.write('Dados do Usuário:', dados)
            else:
                st.error('Usuário ou senha inválidos.')
        except Exception as e:
            st.error(f'Ocorreu um erro ao realizar o login: {e}')
    else:
        st.warning('Por favor, preencha todos os campos.')
