	
import requests
import json
import time
import requests.packages.urllib3
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth  # for Basic Auth

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable insecure https warnings

class spark_api:


	def __init__(self, spark_auth, spark_url):
  
		self.auth = 'Bearer ' + spark_auth
		self.url = spark_url
		self.headers = self.set_headers()



	def set_headers(self):
		spark_header = {'authorization':self.auth, 'Content-Type': 'application/json; charset=utf-8'}
		return spark_header


	def create_Spark_Room(self, spark_room):
	

	    """
	    This function will create a Spark room.
	    Input - the room name
	    Output - the room Id
	    """
		
	    payload = {'title': spark_room}
	    url = self.url + '/rooms'
	    # header = {'content-type': 'application/json', 'Authorization': self.auth}
	    room_response = requests.post(url, data=json.dumps(payload), headers=self.headers)
	    print(room_response)
	    room_json = room_response.json()
	    room_number = room_json['id']
	    print('Created Room with the name:  ', spark_room)
	    return room_number


	def add_Membership(self, room_id, email):


		"""
	    This function will add membership to the room with the room Id
	    Input - room Id and email address to invite
	    Output - None
		"""

		payload = {'roomId': room_id, 'personEmail': email, 'isModerator': 'true'}
		url = self.url + '/memberships'
	    # header = {'content-type': 'application/json', 'authorization': self.auth}
		member_response = requests.post(url, data=json.dumps(payload), headers=self.headers, verify=False)
		print("Invitation sent to:  ", email)
	

	

	def post_Message(self, room_id, message):


		"""
		This function will post a message in a Spark room
		Input - Room Id and message to be posted
		"""
		payload = {'roomId': room_id, 'text': message}
		url = self.url + '/messages'
		# # header = {'content-type': 'application/json', 'authorization': self.auth}
		# member_response = requests.post(url, data=json.dumps(payload), headers=self.headers, verify=False)
		# payload = {'roomId':room_id,'text':message}
		response = requests.post(url, data=json.dumps(payload), headers=self.headers)
		print(response.text)

		print(response)
		print("Message posted:  ", message)


	    




