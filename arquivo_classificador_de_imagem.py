#01.Importar as bibliotecas necessárias
import tensorflow
import keras
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


#02.Criando função para classificar frente
def funcao_classificar_imagem(img, keras_model):

  np.set_printoptions(suppress=True)
  model = load_model('keras_model.h5')
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = img
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.ANTIALIAS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
  data[0] = normalized_image_array
  prediction = model.predict(data)

  return np.argmax(prediction)
