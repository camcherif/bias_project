import nltk
#nltk.download()
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from statistics import mean

def senti(autosugg_list):
    scores = []
    sia = SentimentIntensityAnalyzer()
    stemmer = SnowballStemmer("english")
    for s in autosugg_list:
        scores.append(sia.polarity_scores(stemmer.stem(s))['compound'])
    return mean(scores)

print(senti(['idiot', 'not small men', 'making headlines for the wrong reasons']))
