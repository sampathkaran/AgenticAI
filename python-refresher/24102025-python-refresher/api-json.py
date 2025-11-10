# # we use this API endpint https://openweathermap.org/api
# import requests
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     "latitude" :1.3521, 
#     "longitude":103.8198, 
#     "hourly": "temperature_2m" 
#     }
# response = requests.get(url, params=params)
# print("Status Code", response.status_code)
# print("Response ", response.text)
  
# data = response.json() # parse JSON
# print("Parsed Response", data)

# # access specific data
# example_value = data["hourly"]["temperature_2m"][1] # access specific data
# print("Example Temperature Value", example_value)

import requests

r = requests.get("https://xkcd.com/533/")
# print(r)
# print(dir(r)) # this will print the methods that we can for the response
print(r.text)