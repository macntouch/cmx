#      Cisco CMX API Wrapper
#               v.02
#
#      Nabeel Rajab (nrajab@cisco.com)
#      Hadil Ghaban (hghaban@cisco.com)
#      Mohammed Almoslem (malmosle@cisco.com)
#              April 2017
#
#              This class provides methods to facilitate
#              the use of the CMX API.
#
#   REQUIREMENTS:
#              Python requests library (python-requests)
#
#   WARNING:
#              This script is meant for educational purposes only.
#              Any use of these scripts and tools is at
#              our own risk. There is no guarantee that
#              they have been through thorough testing in a
#              comparable environment and we are not
#              responsible for any damage or data loss
#              incurred with their use.
#
#   INFORMATION:
#              If you have further questions about this API and script, please contact GVE. Here are the contact details:
#                              For internal Cisco employees, please contact GVE at http://go2.cisco.com/gve
#                              For Cisco partners, please open a case at www.cisco.com/go/ph
import requests
from requests.auth import HTTPBasicAuth
import json


class cmx_api:
    def __init__(self, server, username, password):
        """
        This function will initialise the class object
        and can be used to set all the internal variables
        for the oobject such as server address, username,
        and password.
        :param server: server hostname or IP
        :param username: user name to access CMX
        :param password: password to access CMX
        """
        self.server = server
        self.auth = HTTPBasicAuth(username, password)
        self.user = username
        self.passw = password
        self.headers = self.set_headers()
    def set_headers(self):
        """
        This function will set the header information for the class object
        to use json formatting and utf-8 coding scheme.
        :return: header info
        """
        cmx_header = {'Content-Type': 'application/json; charset=utf-8'}
        return cmx_header
    def get_active_client_by_mac(self):
        """
        This function will retrieve the mac addresses for all the active
        clients connected to the CMX system.
        :return: list of mac addresses
        """
        url = self.server+"/api/location/v2/clients/active/"
        response = requests.request("GET", url, verify=False, headers=self.headers, auth=self.auth)
        jresp = response.json()
        return (jresp)
    def get_zone_list(self, zoneID):
        """
        This function will retrieve the list of zones configured in the CMX
        system.
        :return: zone/area details
        """
        url = self.server+"/api/config/v1/heterarchy/"
        parameters = {"areaFilter":zoneID}
        response = requests.request("GET", url, verify=False, params=parameters, headers=self.headers, auth=self.auth)
        jresp = response.json()
        return (jresp['heterarchy'])
    def get_active_client_count(self):
        """
        This function will find out the number of active clients within
        the CMX system
        :return: number of clients
        """
        url = self.server+"/api/location/v2/clients/count/"
        response = requests.request("GET", url, verify=False, headers=self.headers, auth=self.auth)
        jresp = response.json()
        return (jresp['count'])
    def get_client_count_per_zone(self, zoneID, yAxis, timeRange, period,
    durationCategories, includeStationary, connectionState, dataType):
        """
        This function will find out number of active clients
        Call to CMX - /api/location/v2/clients/count
        :param zoneID: id number of the zone
        :param yAxis: devices or visits
        :param timeRange: window of interest in hours and mins
        :param period: window of interest in dates
        :param durationCategories: range defining dwell time
        :param includeStationary: stationary devices true or false
        :param connectionState: connected or detected devices
        :param dataType: type of data
        :return: zone details for connected clients
        """
        url = self.server+"/api/analytics/v1/overview"
        parameters = {"areas":zoneID, "yAxis":yAxis, "timeRange":timeRange,
        "period":period, "durationCategories":durationCategories,"includeStationary":includeStationary,
        "connectionState":connectionState,"type":dataType}
        response = requests.request("GET", url, verify=False, params=parameters, headers=self.headers, auth=self.auth)
        jresp = response.json()
        return (jresp)
