from yahoo_bias import yahoo_autosugg
from google_query import google_q
from sentiment import senti 
import pandas as pd, pycountry
import time

def main():
    var = input("Enter your query: ")
    country = ["Canada","United States", "United Kingdom", "France", "Australia", "New Zealand", "Singapore", "Japan", "South Africa", "Philippines"]
    senti_avg_google = []
    senti_avg_yahoo = []
    pyc = []

    for c in country:
        time.sleep(5)
        r = pycountry.countries.get(name=c).alpha_2
        pyc.append(r)
        print(c)

        #getting the autosuggestions from google and yahoo 
        #getting sentiment analysis for google and yahoo autosugestion
        #append to the list for respective search engines
        senti_avg_google.append([senti((google_q(var, r)[0]).tolist()), r])
        senti_avg_yahoo.append([(senti(yahoo_autosugg(var, r))), r])

        
        

    #call heatmap function and display the figure 



    


if __name__ == "__main__":
    main()