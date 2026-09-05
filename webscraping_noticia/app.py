import requests
import pandas as pd
import streamlit as st
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Notícias da UFRN sobre a EAJ",
    layout="wide"
)

st.title("📢 Notícias da UFRN sobre a EAJ")
st.write("Clique no botão abaixo para coletar as notícias relacionadas à EAJ.")

# Botão para iniciar a coleta
if st.button("🔍 Coletar Notícias"):

    with st.spinner("Coletando notícias..."):

        url = "https://webcache01-producao.info.ufrn.br/admin/portal-ufrn/wp-json/wp/v2/noticias-busca/"

        pagina = 1
        noticias = []

        while True:

            parametros = {
                "per_page": 100,
                "page": pagina,
                "termo": "EAJ",
                "tags": "",
                "data": ""
            }

            try:
                resposta = requests.get(
                    url,
                    params=parametros,
                    headers={"User-Agent": "Mozilla/5.0"},
                    timeout=20
                )

                if resposta.status_code != 200:
                    st.error(f"Erro HTTP: {resposta.status_code}")
                    break

                dados = resposta.json()

                if not dados:
                    break

                for noticia in dados:

                    try:
                        timestamp = int(
                            noticia["acf"]["data_de_publicacao"]
                        )

                        ano = datetime.fromtimestamp(
                            timestamp
                        ).year

                        link = noticia["link"]

                        titulo = noticia.get(
                            "title",
                            {}
                        ).get(
                            "rendered",
                            "Sem título"
                        )

                        noticias.append({
                            "Ano": ano,
                            "Título": titulo,
                            "Link": link
                        })

                    except Exception:
                        continue

                pagina += 1

            except Exception as erro:
                st.error(f"Erro ao acessar a API: {erro}")
                break

    if len(noticias) > 0:

        # DataFrame
        df = pd.DataFrame(noticias)

        # Salvar arquivo TXT
        with open(
            "noticias_eaj.txt",
            "w",
            encoding="utf-8"
        ) as arquivo:

            for _, linha in df.iterrows():
                arquivo.write(
                    f"{linha['Ano']} | {linha['Link']}\n"
                )

        st.success(
            f"✅ {len(df)} notícias encontradas!"
        )

        st.subheader("📋 Dados coletados")
        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader(
            "📊 Quantidade de notícias por ano"
        )

        quantidade_por_ano = (
            df["Ano"]
            .value_counts()
            .sort_index()
        )

        st.bar_chart(quantidade_por_ano)

        st.subheader("📈 Tabela Resumida")

        resumo = (
            quantidade_por_ano
            .reset_index()
        )

        resumo.columns = [
            "Ano",
            "Quantidade"
        ]

        st.dataframe(
            resumo,
            use_container_width=True
        )

    else:
        st.warning(
            "Nenhuma notícia foi encontrada."
        )