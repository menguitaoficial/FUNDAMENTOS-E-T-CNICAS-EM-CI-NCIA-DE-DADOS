# Webscraping Wikipédia

Projeto desenvolvido para a disciplina de Fundamentos e Técnicas em Ciência de Dados.

## Objetivo

Realizar webscraping em páginas da Wikipédia utilizando Requests + BeautifulSoup, gerar uma nuvem de palavras e contabilizar a frequência de uma palavra informada pelo usuário.

## Tecnologias Utilizadas

* Python
* Requests
* BeautifulSoup
* Streamlit
* NLTK
* WordCloud
* Matplotlib

## Funcionalidades

* Busca de 5 páginas da Wikipédia.
* Tratamento de erro 404.
* Remoção de stopwords.
* Geração de nuvem de palavras.
* Contagem de frequência de palavras.
* Medição do tempo de execução.

## Como Executar

Instalar as dependências:

pip install -r requirements.txt

Executar o aplicativo:

streamlit run app.py

## Exemplo de Entrada

Python,Java,Brasil,Inteligência Artificial,Ciência de Dados

Palavra:

dados
