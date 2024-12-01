import sys
import os
import streamlit as st
from streamlit_cookies_controller import CookieController


controller = CookieController()

cookies = controller.getAll()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controllers.LoginController import Login

st.set_page_config(
    page_title="Norte Auto Peças - Painel de meta",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.image('./Images/Logo.png')


def is_logged_in():
    user_status = cookies.get("user_status")
    if not user_status: 
        return False
    return user_status

def LoginPage():
    if is_logged_in():
        st.success(f'Bem-vindo(a) de volta, {cookies.get("username")}!')
        return

    username = st.text_input('Usuário', value='', placeholder='Digite seu nome de usuário')
    password = st.text_input('Senha', value='', placeholder='Digite sua senha', type='password')

    if st.button('Entrar'):
        if username and password:
            login_user = Login(username, password)
            try:
                data = login_user.execute_query()
                if not data.empty:
                    controller.set("username", username) 
                    controller.set('user_status', "True")
                    controller.set('password', password)
                    controller.set('user_id', str(data["ID"]))
                    st.success(f'Bem-vindo(a), {username}!')
                else:
                    st.error('Usuário ou senha inválidos.')
            except Exception as e:
                st.error(f'Ocorreu um erro ao realizar o login: {e}')
        else:
            st.warning('Por favor, preencha todos os campos.')

def logout_user():
    controller.remove('user_status')
    controller.remove('username')
    controller.remove('password')
    controller.remove('user_id')

if __name__ == "__main__":
    LoginPage()
