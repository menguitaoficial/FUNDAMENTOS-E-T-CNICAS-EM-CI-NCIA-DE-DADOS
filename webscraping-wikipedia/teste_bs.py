import requests
from bs4 import BeautifulSoup


def buscar_wikipedia(termo):
    url = "https://pt.wikipedia.org/wiki/" + termo.replace(" ", "_")

    headers = {
        "User-Agent": "WebScrapingWikipedia/1.0 (projeto academico)"
    }

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 404:
        print("Página não encontrada.")
        return ""

    soup = BeautifulSoup(resposta.text, "html.parser")

    texto = soup.get_text()

    return texto


texto = buscar_wikipedia("TermoQueNaoExiste123456789")

print(texto)