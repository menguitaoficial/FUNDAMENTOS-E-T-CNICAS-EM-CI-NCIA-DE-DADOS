import requests
from bs4 import BeautifulSoup


def buscar_wikipedia(termo):

    url = "https://pt.wikipedia.org/wiki/" + termo.replace(" ", "_")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
    }

    try:
        resposta = requests.get(
            url,
            headers=headers,
            timeout=10
        )

    except requests.RequestException:
        return None

    if resposta.status_code == 404:
        return None

    if resposta.status_code != 200:
        return None

    soup = BeautifulSoup(
        resposta.text,
        "html.parser"
    )

    # Remover partes desnecessárias da página
    for elemento in soup(
        ["script", "style", "nav", "footer"]
    ):
        elemento.decompose()

    # Pegar o texto da página
    texto = soup.get_text(
        separator=" ",
        strip=True
    )

    return texto 