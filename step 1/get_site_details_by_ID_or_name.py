import requests

url = "https://msesandbox.cisco.com:8081/api/config/v1/sites/"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'cache-control': "no-cache",
    'postman-token': "dd3ca964-9532-5454-8cd3-6cac4d81e352"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)