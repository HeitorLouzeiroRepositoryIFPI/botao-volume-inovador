import streamlit as st

# Título da aplicação
st.title("🎚️ Controle de Volume interativo")

# Inicializa o estado da sessão para o volume
if "som" not in st.session_state:
    st.session_state.som = 50  # Valor inicial do volume

# Funções para ajustar o volume


def aumentar_som():
    if st.session_state.som < 100:
        st.session_state.som += 5


def diminuir_som():
    if st.session_state.som > 0:
        st.session_state.som -= 5


# Layout da aplicação
st.write("Clique nos botões abaixo para ajustar o volume do som:")

# Botões para aumentar e diminuir o volume do som
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.button("➖ Diminuir", on_click=diminuir_som, use_container_width=True)

with col3:
    st.button("➕ Aumentar", on_click=aumentar_som, use_container_width=True)

# Exibir o valor atual do volume
st.markdown(
    # noqua
    f"<h2 style='text-align: center;'>🔊 Volume Atual: {st.session_state.som}</h2>",
    unsafe_allow_html=True,
)

# Barra de progresso visual
st.progress(st.session_state.som / 100)
