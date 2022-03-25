import requests, json

var = input("Enter your query: ")

URL = "http://suggestqueries.google.com/complete/search?client=firefox&q=" + var
headers = {'User-agent':'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
result = json.loads(response.content.decode('utf-8'))
i=1
result = result[1]
for query in result[1:]:
    result[i] = query.replace(result[0] + ' ', '')
    i+=1
print(result[1:])