from yahoo_bias import yahoo_autosugg
from google_query import google_q
from sentiment import senti 
import pandas as pd, pycountry
from heat_map import heat_map

def main():
    var = input("Enter your query: ")
    country = ["Canada", "United States", "Mexico", "Peru", "Paraguay", "Colombia", "Chile", 
               "Argentina", "Brazil", "Morocco", "Algeria", "Tunisia", "Libya", "Egypt", 
               "Mauritania", "Nigeria", "Cameroon", "Sudan", "Senegal", "Burkina Faso", "Angola", 
               "Botswana", "Kenya", "Ethiopia", "Somalia", "Zambia", "Zimbabwe", "South Africa", 
               "Madagascar", "Portugal", "Spain", "United Kingdom", "France", "Germany", 
               "Italy", "Switzerland", "Belgium", "Denmark", "Norway", "Netherlands", "Sweden", 
               "Latvia", "Lithuania", "Slovenia", "Romania", "Poland", "Ukraine", "Turkey", 
               "United Arab Emirates", "India", "Sri Lanka", "Singapore", "Thailand", "China", 
               "Japan", "Philippines", "Australia", "New Zealand"]
    senti_avg_google = []
    senti_avg_yahoo = []
    pyc = []
    
    print('Fetching data from:\n')
    for c in country:
        r = pycountry.countries.get(name=c).alpha_2
        pyc.append(r)
        print(c)

        #getting the autosuggestions from google and yahoo 
        #getting sentiment analysis for google and yahoo autosugestion
        #append to the list for respective search engines
        google_query = (google_q(var, r)[0]).tolist()
        #evaluating with senti if query did not return empty array:
        if google_query:
            senti_avg_google.append([senti((google_q(var, r)[0]).tolist()), r])
        if yahoo_autosugg(var, r):
            senti_avg_yahoo.append([(senti(yahoo_autosugg(var, r))), r])

    heat_map(country, var, senti_avg_google, senti_avg_yahoo)

    #call heatmap function and display the figure 


if __name__ == "__main__":
    main()