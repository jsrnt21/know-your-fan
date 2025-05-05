Instruções para instalar dependências e executar o app localmente:

# Instalação

### Pré-requisitos
- Python 3.10+
- pip

### Instale as dependências
- pip install -r requirements.txt

- Instale o Tesseract OCR em: https://github.com/tesseract-ocr/tesseract

    Certifique-se de que o caminho para o executável está no PATH ou defina manualmente no código:
        - pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

- Execute o aplicativo: streamlit run app.py