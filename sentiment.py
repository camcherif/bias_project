import nltk
#nltk.download() 
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer
from statistics import mean

#senti perform sentiment analysis with nltk on the list of autosuggestions
def senti(autosugg_list):
    if not autosugg_list:
        return 0
    scores = []
    sia = SentimentIntensityAnalyzer()
    stemmer = SnowballStemmer("english")
    for s in autosugg_list:
        #compound < 0 when the sentiment is negative and >0 when positive
        scores.append(sia.polarity_scores(stemmer.stem(s))['compound']) 
    return mean(scores) #mean sentiment for the autosuggestion list
