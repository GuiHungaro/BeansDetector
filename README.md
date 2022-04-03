![alt text](logo2.png)

# Red Hot Chili Beans

Red Hot Chili Beans é um aplicativo rodando na nuvem utilizando a a biblioteca [Streamlit](https://streamlit.io/) (Python) para rodar um modelo de classificação de imagens utilizando o o [Teachable Machine do Google](https://teachablemachine.withgoogle.com/). 

## Para acessá-lo [Clique aqui](https://share.streamlit.io/guihungaro/beansdetector/main). 

----- 

## 01.Compreensão do Negócio.

Você sabia que o Brasil é o quarto maior produtor de grãos do mundo porém todo o processo de classificação de grãos é feito por um profissional?
Já que os critérios avaliados dependem da avaliação humana e podem ser divergentes, não há um padrão de análise. 

Se o grão de soja não estiver de acordo com parâmetros estabelecidos, o agricultor pode ter o desconto no pagamento da carga.

O Brasil exportou em 2021 86,628 milhões de toneladas de soja em grão, 5,2% mais que no ano anterior. 
Se uma API de classificação de grãos atingisse 20% do total exportado, pagando R$ 0,5 por saca (60kg), teria um faturamento de R$ 144.380.000,00 em 2021.

Neste MVP exploramos essa oportunidade no mundo das AgriTech's!

----

## 02.Sobre o projeto.

São mais de 13 classes e subtipos de feijão, porém para este **MVP** nós treinamos apenas 5 classes, sendo elas:

* 01.Feijão branco
* 02.Feijao carioca
* 03.Feijao fradinho
* 04.Feijao preto
* 05.Feijao rajado

![alt text](training_model.png)

A ideia é nesse aplicativo é que o usuário possa acessar pelo celular, tablet, computador e realizar o upload da foto do feijão que deseja classificar.

![alt text](upload.png)

Depois do upload, o modelo irá rodar e classificar qual o tipo de feijão está presente na foto.

![alt text](feijao.png)

---

# **OBSERVAÇÃO:**

* Este modelo foi treinado com fotos aleatórias da internet. Ele não vai estar performando no melhor desempenho possível pois foi utilizado uma base de treino fraca. **Garbage in - Garbage out**.

* Este projeto é uma forma de validar a idéia e unir a biblioteca Streamlit com o Teachable Machine. Não tem aplicação comercial neste formato.

