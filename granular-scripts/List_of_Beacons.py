import requests



def ListOfBeaacons ():

url = "https://msesandbox.cisco.com:8081/api/location/v1/beacon"

headers = {
    'authorization': "Basic bGVhcm5pbmc6bGVhcm5pbmc=",
    'cache-control': "no-cache",
    'postman-token': "7fd2e8f5-84fd-bb9f-c56b-d8dda0cfbdb3"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)