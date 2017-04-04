

def get_active_client_count(server):

	url = self.server+"/api/location/v2/clients/count"
	response = requests.request("GET", url, headers=self.headers)
	print(response.text)