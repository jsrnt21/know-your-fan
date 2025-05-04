from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Exemplos de textos e seus rótulos (1 = fã de e-sports, 0 = genérico)
exemplos = [
    "amo a FURIA", "csgo é minha vida", "vou em todos os majors", "assisto stream de valorant",
    "jogo lol todo dia", "sou pro player", "adoro esports", "participei de campeonato online",
    "acompanho o CBLOL", "tenho coleção de camisetas da FURIA" "cs",

    "gosto de cozinhar", "minha família é minha vida", "adoro filmes", "viajo muito a trabalho",
    "sou apaixonado por jardinagem", "escuto música clássica", "sou contador de empresas",
    "prefiro futebol", "não entendo de jogos", "uso redes sociais só pra família"
]

rotulos = [1]*10 + [0]*10  # 10 fãs, 10 genéricos

# Criar pipeline de modelo com vetorizador + Naive Bayes
modelo = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB())
])

# Treinar
modelo.fit(exemplos, rotulos)

# Salvar modelo em um arquivo .pkl
joblib.dump(modelo, 'modelo_ia_esports.pkl')

print("✅ Modelo treinado e salvo com sucesso como 'modelo_ia_esports.pkl'")
