import requests

#r = requests.get("https://api.weatherapi.com/v1/current.json?key=a069cc622063427abd692423261806&q=London&aqi=yes")
city = input("Enter the city to check temperature: ")
r = requests.get("https://api.weatherapi.com/v1/current.json?", params = {'key': "a069cc622063427abd692423261806", 'q' : city})
print(r)
#print(dir(r))
#print(r.text)

# r.ok
# r.status_code
# r.content
# r.headers
# payload - dict type
r_dict = r.json()
print(r_dict['current']['temp_c'])
print(r_dict['current']['condition']['text'])
# requests.post(data = payload)
# r.url
# r_dict = r.json()