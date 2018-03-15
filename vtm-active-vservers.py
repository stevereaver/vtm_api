#!/usr/bin/python
import requests, json, pprint
from requests.auth import HTTPBasicAuth
from pprint import pprint


url = 'https://vtm-test:9070/api/tm/5.1/config/active/vservers'

requests.packages.urllib3.disable_warnings()
response = requests.get(url, auth=HTTPBasicAuth('admin', 'reaver1'),verify=False)

#print response.json()
parsed_response = json.loads(response.text)
print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))


# The following will print the 1st (0) 'children' in the dict, then print the value stored there
print parsed_response['children'][0]['href']
print parsed_response['children'][0]['name']
