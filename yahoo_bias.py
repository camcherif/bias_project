import requests
import re
import json
import pandas as pd, pycountry

def yahoo_autosugg(feature, loca):

  #so basically this is the url I found to get yahoo autosuggestion for women
  #there's no api available and this is the only feasible solution I found lmao
  #we just need to replace women in the url by the feature we're actually looking for and it works great
  feature = feature.replace(' ', '%20')
  if str(loca) == "gb":
    loca = "uk"
  url = "https://"+loca+".search.yahoo.com/sugg/gossip/gossip-"+loca+"-ura/?pq="+feature+"&command="+feature+"&t_stmp=1648056743&callback=YAHOO.SA.apps%5B0%5D.cb.sacb0&l=1&bm=3&output=sd1&nresults=10&geoid=23897142&.crumb=zDg1NmBdWJ0&f=1&appid=ca.search.yahoo.com&bck=9kb8gcdh39es9%26b%3D3%26s%3D1m&csrcpvid=InOFpTEwLjGaLRBjYjS7iQLiNzQuNQAAAAD5R1sM&vtestid=&mtestid=24576%3DD1114&spaceId=2114721002"

  try:
    r = requests.get(url)
  except:
    return []
  
  if int(r.status_code)>300:
        return []

  #looks for the autosuggestions 
  att = att = re.findall(r'(?<="(k)":)"((.*?))"',r.text)
  output=[]

  if att: #if not empty
    for i in att: #for the autosuggest string found
      s = i[1]
      if s:
        output.append(s) #append the result to the list

  return output
