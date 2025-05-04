import streamlit as st
import re
import pytesseract
from PIL import Image

# Função para verificar se o texto é relacionado a e-sports
def verificar_esports(texto):
    termos_esports = ['FURIA', 'CSGO', 'valorant', 'esports', 'gaming', 'pro player', 'Major', 'game', 'e-sports']
    for termo in termos_esports:
        if re.search(r'\b' + re.escape(termo) + r'\b', texto, re.IGNORECASE):
            return True
    return False

# Função para extrair texto de uma imagem usando o Tesseract
def extrair_texto(imagem):
    texto = pytesseract.image_to_string(imagem)
    return texto

# Título do aplicativo
st.title('Validação de Perfil de Fã de E-sports')

# Campos para coletar dados
nome = st.text_input('Nome:')
cpf = st.text_input('CPF:')
endereco = st.text_area('Endereço:')

# Campos para redes sociais, com '@' pré-fixado
twitter = st.text_input('Twitter (sem @):')
instagram = st.text_input('Instagram (sem @):')

# Exibição de dados com o '@' pré-fixado nas URLs
if nome and cpf and endereco and twitter and instagram:
    twitter_url = f"https://twitter.com/{twitter}"  # Monta a URL do Twitter
    instagram_url = f"https://www.instagram.com/{instagram}"  # Monta a URL do Instagram
    
    st.subheader('Resumo dos Dados Coletados:')
    st.write(f"**Nome:** {nome}")
    st.write(f"**CPF:** {cpf}")
    st.write(f"**Endereço:** {endereco}")
    st.write(f"**Twitter:** {twitter_url}")
    st.write(f"**Instagram:** {instagram_url}")
else:
    st.warning('Preencha todos os campos para ver o resumo dos dados.')

# Campo para upload de imagem (documento)
uploaded_file = st.file_uploader("Carregue uma imagem ou documento para extração de texto:", type=["jpg", "jpeg", "png"])

# Verificação de upload de arquivo
if uploaded_file is not None:
    st.write("Arquivo carregado com sucesso!")
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Imagem carregada.", use_container_width=True)

    # Extrair texto da imagem usando o Tesseract
    try:
        texto_extraido = extrair_texto(imagem)
        st.subheader("Texto Extraído da Imagem:")
        st.write(texto_extraido)
    except Exception as e:
        st.error(f"Erro ao extrair texto da imagem: {e}")
else:
    st.write("Aguardando upload de imagem...")

# Campo para digitar o texto a ser validado
texto_usuario = st.text_area('Digite um breve resumo sobre quem você é, do que gosta, o que faz:', '')

if texto_usuario:
    if verificar_esports(texto_usuario):
        st.write("✅ O texto está relacionado a e-sports.")
    else:
        st.write("❌ O texto não está relacionado a e-sports.")
