import requests
from bs4 import BeautifulSoup
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def buscar_wikipedia(termo):
    url = "https://pt.wikipedia.org/wiki/" + termo.replace(" ", "_")

    headers = {
        "User-Agent": "WebScrapingWikipedia/1.0 (projeto academico)"
    }

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 404:
        return ""

    soup = BeautifulSoup(resposta.text, "html.parser")

    texto = soup.get_text()

    return texto


inicio = time.perf_counter()

entrada = input("Digite 5 termos separados por vírgula: ")

termos = entrada.split(",")

encontradas = 0
palavras_limpas = []

for termo in termos:
    termo = termo.strip()

    print(f"\nBuscando: {termo}")

    texto = buscar_wikipedia(termo)

    if texto:
        print("✅ Página encontrada.")
        encontradas += 1
        palavras_limpas.append(texto)
    else:
        print("❌ Página não encontrada.")


print(f"\nTotal de páginas encontradas: {encontradas}")


fim = time.perf_counter()

tempo = fim - inicio

print()
print(f"Tempo de execução: {tempo:.4f} segundos")


nuvem = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(
    " ".join(palavras_limpas)
)


plt.figure(figsize=(15, 7))

plt.imshow(
    nuvem,
    interpolation="bilinear"
)

plt.axis("off")

plt.show()