#01.Importar as funções e bibliotecas necessárias.

from arquivo_classificador_de_imagem import funcao_classificar_imagem
import streamlit as st
from PIL import Image


#Criando a chave de acesso
def check_password_username():
  #Criando a verificação do usuário
  def username_entered():
    if st.session_state["username"] == st.secrets["username"]:
       st.session_state["username_correct"] = True
       del st.session_state["username"]  # não salvar o usuário
    else:
      st.session_state["username_correct"] = False
    
  #Criando a verificação da senha
  def password_entered():
    if st.session_state["password"] == st.secrets["password"]:
      st.session_state["password_correct"] = True
      del st.session_state["password"]  # não salvar a senha
    else:
      st.session_state["password_correct"] = False

  #Plotando o input de usuário e a senha         
  if "username_correct" and "password_correct" not in st.session_state:
    st.text_input("Nome de usuário", on_change=username_entered, key="username")
    st.text_input("Senha", type="password", on_change=password_entered, key="password")
    return False
  
  #Caso o usuário não esteja correto
  elif not st.session_state["username_correct"]:
    st.text_input("Nome de usuário", on_change=username_entered, key="username")
    st.text_input("Senha", type="password", on_change=password_entered, key="password")
    return False

  #Caso a senha não esteja correta      
  elif not st.session_state["password_correct"]:
    st.text_input("Nome de usuário", on_change=username_entered, key="username")
    st.text_input("Senha", type="password", on_change=password_entered, key="password")
    st.error("😕 Usuário ou senha incorreto!")
    return False

  #Caso os dois estejam corretos  
  else:
    return True

if check_password_username():

  #02.Logo aplicativo.

  logo = Image.open("logo2.png")
  st.image(logo, caption='', use_column_width=True)

  #03. Foto da frente do veículo.
  st.title("Classificador de Feijões:")
  foto_frente = st.checkbox("Fazer upload.", key=1)
  if foto_frente:

    uploaded_file = st.file_uploader("Escolha um arquivo", type=None, key=1)
    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='', use_column_width=True)
        st.write("Classificando...")
        label = funcao_classificar_imagem(image, 'keras_model.h5')

        if label == 0:
          st.title("Feijão Branco.")

        elif label == 1:
          st.title("Feijão Carioca.")

        elif label == 2:
          st.title("Feijão Fradinho.")

        elif label == 3:
          st.title("Feijão Preto.")

        else:
          st.title("Feijão Rajado.")
