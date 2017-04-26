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


import json
import time
from cmx_api import cmx_api
from spark_api import spark_api
import requests
from requests.auth import HTTPBasicAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def loadSettings(settingsFile):
    """Reads settings file into an list.

    :param settingsFile: the name of the settings file e.g. ``'settings.txt'``
    :type settingsFile: string
    :returns: the newly-created list
    """

    with open(settingsFile,'r') as f:
        settings = f.readlines()
    f.close()

    return settings

def pprint(json_data):
    """
    Pretty print JSON formatted data
    :param json_data:
    :return:
    """

    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))

def main():
    appSettings = loadSettings("../settings.txt")

    username = appSettings[0].rstrip()
    password = appSettings[1].rstrip()
    cmx_server = appSettings[2].rstrip()
    spark_auth = appSettings[10].rstrip()
    spark_server = appSettings[6].rstrip()
    cashier_room_id = appSettings[9].rstrip()

    cmx_obj = cmx_api(cmx_server, username, password)
    spark_obj = spark_api(spark_auth, spark_server)

    while(1):
        time.sleep(120)

        customer_count = cmx_obj.get_client_count_per_zone(58, "absoluteVisits", "now", "today",
        "5-480", "true", "all", "deviceDwell")["value"]["previousTimeRange"]["breakdown"][0]["value"]

        print(customer_count)

        if customer_count >= 5:
            message = "NOTICE: Queue gathering at check-out. Please verify and open till if needed!"
            spark_obj.post_Message(cashier_room_id, message)

if __name__ == '__main__':
    main()
