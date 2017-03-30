import requests

url = "https://msesandbox.cisco.com:8081/api/location/v2/clients/count"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'cache-control': "no-cache",
    'postman-token': "481994fc-cab0-7cd0-669d-f9e1e5f06285"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)