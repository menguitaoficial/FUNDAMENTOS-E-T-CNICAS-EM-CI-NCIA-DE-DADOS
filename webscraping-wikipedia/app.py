import re
import streamlit as st
from scraping_bs import buscar_wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Wikipedia Web Scraping",
    page_icon="🔎"
)


st.title("🔎 Wikipedia Web Scraping")

st.write(
    "Extração e análise de textos da Wikipédia"
)


entrada = st.text_input(
    "Digite 5 termos separados por vírgula:"
)


palavra = st.text_input(
    "Digite uma palavra para pesquisar:"
)


executar = st.button(
    "Executar scraping"
)


if executar:

    termos = [
        termo.strip()
        for termo in entrada.split(",")
        if termo.strip()
    ]

    if len(termos) != 5:

        st.error(
            "Digite exatamente 5 termos."
        )

    else:

        textos = []

        for termo in termos:

            st.write(
                f"🔎 Buscando: **{termo}**"
            )

            texto = buscar_wikipedia(termo)

            if texto is None:

                st.error(
                    f"❌ Página não encontrada: {termo}"
                )

            else:

                textos.append(texto)

                st.success(
                    f"✅ Página encontrada: {termo}"
                )

        if textos:

            texto_completo = " ".join(textos)

            palavras = re.findall(
                r"\b\w+\b",
                texto_completo.lower()
            )

            palavras_limpas = [
                palavra
                for palavra in palavras
                if len(palavra) > 3
            ]

            nuvem = WordCloud(
                width=1000,
                height=500,
                background_color="white"
            ).generate(
                " ".join(palavras_limpas)
            )

            st.subheader(
                "☁️ Nuvem de palavras"
            )

            fig, ax = plt.subplots(
                figsize=(15, 7)
            )

            ax.imshow(
                nuvem,
                interpolation="bilinear"
            )

            ax.axis("off")

            st.pyplot(fig)

            if palavra.strip():

                quantidade = palavras.count(
                    palavra.lower().strip()
                )

                st.subheader(
                    "🔎 Pesquisa de palavra"
                )

                st.write(
                    f'A palavra "{palavra}" aparece '
                    f'{quantidade} vezes.'
                ) 