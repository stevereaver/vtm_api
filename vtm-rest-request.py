#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
import json

# curl --insecure --user admin:reaver1 https://vtm-test:9070/api/tm/5.1/config/active/|json_pp
 
url = 'https://vtm-test:9070/api/tm/5.1/config/active'

#r = requests.get('<MY_URI>', headers={'Authorization': 'TOK:<MY_TOKEN>'})
# admin:xxxxxx   BASE64 =  YWRtaW46cmVhdmUx

requests.packages.urllib3.disable_warnings()
#response = requests.get(url, headers={'Authorization': 'Basic:YWRtaW46cmVhdmUx'},verify=False)
response = requests.get(url, auth=HTTPBasicAuth('admin', 'xxxxxx'),verify=False)
#print response.text
print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
