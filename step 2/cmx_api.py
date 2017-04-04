import requests

class cmx_api:

    def __init__(self, server, key):
        self.server = server
        self.headers = set_headers(key)

    def set_headers(key):
    	accessToken_hdr = 'Bearer ' + key
    	cmx_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    	return (cmx_header)

    def get_history_of_client_by_macaddress(server, macaddr, date):
        url = self.server+"/api/location/v1/history/clients/"
        parameters = {"macaddress":macaddr, "date":date}
        response = requests.request("GET", url, params=parameters, headers=self.headers)
        print(response.text)

    def get_site_details_by_ID_or_name():

        url = self.server+"/api/config/v1/sites/"
        response = requests.request("GET", url, headers=self.headers)

        print(response.text)

    def list_of_beacons_present_on_a_floor(floorrefid):
        url = self.server+"/api/location/v1/beacon/floor/"
        parameters = {"floorrefid":floorrefid}
        response = requests.request("GET", url, headers=self.headers)
        print(response.text)
