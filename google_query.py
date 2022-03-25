#refs: https://github.com/GeneralMills/pytrends#related-queries and https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
#   and https://pypi.org/project/pycountry/
#
#______________

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

#suggestions and data presentation
suggestions = pytrend.related_queries().get(var)
top = suggestions.get('top')
rising = suggestions.get('rising')
print(top.head())
print(rising.head())