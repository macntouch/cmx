import requests

url = "https://msesandbox.cisco.com:8081/api/config/v1/maps/image"

headers = {
    'campusname': "asdf",
    'buildingname': "asdf",
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'floorname': "asdf",
    'cache-control': "no-cache",
    'postman-token': "0d56dab7-680e-86bb-1189-3fd4ad926174"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)