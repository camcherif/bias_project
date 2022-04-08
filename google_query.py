#refs: https://github.com/GeneralMills/pytrends#related-queries and https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
#   and https://pypi.org/project/pycountry/
#
#_______________

import subprocess, sys, importlib

#checking if modules are installed, else install
packages = ["pandas",  "pycountry", "pytrends"]
for package in packages:
    if importlib.util.find_spec(package) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import pandas as pd, pycountry
from pytrends.request import TrendReq

#getting input: var is query, country is self-explanatory
def google_q(var, country):
    #getting 2-letter code of country
    country = pycountry.countries.get(name=country).alpha_2

    #building trend request
    pytrend = TrendReq(hl="en-US", tz=300)
    pytrend.build_payload(kw_list=[var], geo=country)

    #suggestions and data presentation of top and rising queries
    related = pytrend.related_queries().get(var)
    #dropping unnecessary columns 'mid' and 'value
    #commenting out suggestions, not using them anymore
    #suggestions = pd.DataFrame(pytrend.suggestions(var)).drop(columns='mid')
    top = related.get('top').drop(columns='value')
    rising = related.get('rising').drop(columns='value')
    #capitalizing titles
    top['query'] = top['query'].str.title()
    rising['query'] = rising['query'].str.title()
    result = [top['query'], rising['query']]
    return result
