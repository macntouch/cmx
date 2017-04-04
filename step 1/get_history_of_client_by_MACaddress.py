import requests

url = "https://msesandbox.cisco.com:8081/api/location/v1/history/clients/"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'cache-control': "no-cache",
    'postman-token': "097ccb99-6261-9254-5e4e-b505372b218d"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)