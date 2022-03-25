import requests, json

var = input("Enter your query: ")
var_space = var.replace(' ', '+')
countries = ["FR","GB","US","CA","ES","ZA","IN"]; 
URL = "http://suggestqueries.google.com/complete/search?client=firefox&q=" + var_space + "&hl=" + countries[0]
headers = {'User-agent':'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
result = json.loads(response.content.decode('utf-8'))[1][1:]
i=0
for query in result:
    result[i] = query.replace(var + ' ', '')
    i+=1
print(result)