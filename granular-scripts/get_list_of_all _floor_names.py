import requests



def ListOfFloorNames ():


url = "https://msesandbox.cisco.com:8081/api/config/v1/maps/floor/list"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'cache-control': "no-cache",
    'postman-token': "7142499a-92e1-da12-f976-6fb8cbf9f8e1"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)