# Arquitetura da Solução

### Componentes

- **Streamlit:** Frontend para entrada de dados e exibição dos resultados.
- **Tesseract OCR:** Reconhecimento de texto em imagens (documentos enviados).
- **Scikit-learn:** IA simples com Naive Bayes treinada com textos de fãs de e-sports.
- **Pipeline:** Pré-processamento + Classificador integrado em um único modelo `.pkl`.

### Fluxo

1. O usuário envia dados e/ou uma imagem.
2. O texto é extraído com OCR.
3. O texto digitado e extraído é analisado com IA.
4. O sistema valida se o perfil é compatível com o perfil de fã.
