#01.Importar as funções e bibliotecas necessárias.

from arquivo_classificador_de_imagem import funcao_classificar_imagem
import streamlit as st
from PIL import Image


#02.Logo aplicativo.

logo = Image.open("logo.png")
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
