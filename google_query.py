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

#getting input
var = input("Enter your query:")
country = input("Enter name of country of choice:")
country = pycountry.countries.get(name=country).alpha_2

#building trend request
pytrend = TrendReq(hl="en-US", tz=300)
pytrend.build_payload(kw_list=[var], geo=country)

#suggestions and data presentation of top and rising queries
related = pytrend.related_queries().get(var)
#dropping unnecessary column 'mid'
suggestions = pd.DataFrame(pytrend.suggestions(var)).drop(columns='mid')
top = related.get('top').drop(0)
rising = related.get('rising').drop(0)
#capitalizing titles
suggestions['title'] = suggestions['title'].str.title()
top['query'] = top['query'].str.title()
rising['query'] = rising['query'].str.title()
print(suggestions.head())
print(top.head())
print(rising.head())
