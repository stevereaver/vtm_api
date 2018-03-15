#!/usr/bin/python
#
# Use this script if you want to add a new node to a pool
#
import requests, json, pprint
from requests.auth import HTTPBasicAuth
from pprint import pprint

poolname = "web-pool"
newnode = "10.5.0.100:80"
#headers = {"Content-Type": "application/json", "Authorization": "Basic YWRtaW46cmVhdmUx"}
headers = {"Content-Type": "application/json",}
url = 'https://vtm-test:9070/api/tm/5.1/config/active/pools/'+poolname
print url

# Authenticate and get JSON
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers,auth=HTTPBasicAuth('admin', 'reaver1'),verify=False)
#response = requests.get(url, headers=headers,verify=False)

#nodeRef = json.loads(response.text)['properties']['basic']['nodes_table']
nodeRef = json.loads(response.text)
#print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
#print nodeRef['properties']['basic']['nodes_table']

# Add the new key to the JSON
nodeRef['properties']['basic']['nodes_table'].append({'node':newnode,'state':'disabled','weight':1})

#print nodeRef['properties']['basic']['nodes_table']

#nodeRef.append({'node':newnode,'state':'disabled','weight':1})

response = requests.put(url,data=json.dumps(nodeRef),headers=headers,auth=HTTPBasicAuth('admin', 'reaver1'),verify=False)
print json.dumps(nodeRef, sort_keys=True, indent=4, separators=(',', ': '))
print response







# The following will print the 1st (0) 'children' in the dict, then print the value stored there
#print parsed_response

#print parsed_response['properties']['basic']['nodes_table']

