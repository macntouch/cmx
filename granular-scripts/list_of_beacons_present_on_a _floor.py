import requests

url = "https://msesandbox.cisco.com:8081/api/location/v1/beacon/floor/"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'floorrefid': "2",
    'cache-control': "no-cache",
    'postman-token': "23375159-ac8c-371e-0614-a21db03cc2d5"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)