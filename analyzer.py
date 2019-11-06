import pickle, random
from leia import SentimentIntensityAnalyzer
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s = SentimentIntensityAnalyzer()

comments = []
negativos = []
positivos = []

mais_negativo = ''
mais_positivo = ''
max_positivo = -1
max_negativo = 1

with open('comments', 'rb') as fp:
    comments = pickle.load(fp)

for comment in comments:
    score = s.polarity_scores(comment)
    if score['compound'] >= 0:
        positivos.append(comment)
    else:
        negativos.append(comment)

    if score['compound'] > max_positivo:
        mais_positivo = comment
        max_positivo = score['compound']

    if score['compound'] < max_negativo:
        mais_negativo = comment
        max_negativo = score['compound']


print(f"Comentários positivos: {len(positivos)}")
print(f"Comentários negativos: {len(negativos)}")
print(f'Comentário mais positivo:')
print(f'{mais_positivo}')
print(f'Comentário mais negativo:')
print(f'{mais_negativo}')
print(f'Comentário negativo do dia :))))')
print(f'{negativos[random.randint(0, len(negativos))]}')