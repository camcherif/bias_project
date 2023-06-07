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

import pandas as pd
from pytrends.request import TrendReq

#getting input: var is query, country is self-explanatory
def google_q(var, country):
    #building trend request
    pytrend = TrendReq(hl="en-US", tz=300)
    pytrend.build_payload(kw_list=[var], geo=country)

    #suggestions and data presentation of top and rising queries
    related = pytrend.related_queries().get(var)
    #creating empty dataframe for exception
    empty_series = pd.Series([])
    #dropping unnecessary columns 'mid' and 'value'
    #and checking if queries get results for autosuggestions
    try: 
        top = related.get('top').drop(columns='value')
    except:
        return [empty_series, empty_series]
    try:
        rising = related.get('rising').drop(columns='value')
    except:
        return [empty_series, empty_series]
    #capitalizing titles
    top['query'] = top['query'].str.title()
    rising['query'] = rising['query'].str.title()
    result = [top['query'], rising['query']]
    return result