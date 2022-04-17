from yahoo_bias.py import yahoo_autosugg
from google_query.py import google_q
from sentiment.py import senti 
import pandas as pd, pycountry

def main():
    var = input("Enter your query: ")
    country = ["canada","united states", "mexico", "united kingdom", "france", "australia", "new zealand", "singapore", "japan", "south africa", "philippines"]
    senti_avg_google = []
    senti_avg_yahoo = []
    pyc = []

    for c in country:
        r = pycountry.countries.get(name=c).alpha_2
        pyc.append(r)

        #getting the autosuggestions from google and yahoo 
        #getting sentiment analysis for google and yahoo autosugestion
        #append to the list for respective search engines
        senti_avg_yahoo.append(senti(yahoo_autosugg(var, r)))
        senti_avg_google.append(senti(google_q(var, r)))


    #what's left: format the lists generated so it fits the input format of the heatmap function
    #call heatmap function and display the figure 



    


if __name__ == "__main__":
    main()