import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from streamlit_cookies_controller import CookieController
import pandas as pd


controller = CookieController()

cookies = controller.getAll()
st.write(cookies)

if cookies.get('user_id'):
    st .write("usuario logado")
