#!/usr/bin/python
#
# Name: 
#   VTM Node Manager 
# Description: 
#   This is a script to set the status of nodes in a virtual traffic manager
# Usage:
#   Usage: vtm-node-manager.py [options]
#
#   Options:
#     -h, --help            show this help message and exit
#     -t HOSTNAME, --hostname=HOSTNAME
#                        hostname of VTM server
#     -o POOLNAME, --poolname=POOLNAME
#                       nodename of VTM server
#     -n NODENAME, --nodename=NODENAME
#                       nodename of VTM server
#     -s STATE, --state=STATE
#                        status to set the node to
#     -u USERNAME, --username=USERNAME
#                        username for VTM authentication
#     -p PASSWORD, --password=PASSWORD
#                        password for VTM authentication
# Author:
#   Stephen Bancroft
# Email:
#   bancroft@tt.com.au
#

import requests, json, pprint,sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t", "--hostname", 
                  action="store", dest="hostName",
                  help="hostname of VTM server")
parser.add_option("-o", "--poolname",
                  action="store",dest="poolName",
                  help="nodename of VTM server")
parser.add_option("-n", "--nodename",
                  action="store",dest="nodeName",
                  help="nodename of VTM server")
parser.add_option("-s", "--state",
                  action="store", dest="state",
                  help="status to set the node to")
parser.add_option("-u", "--username",
                  action="store", dest="userName",
                  help="username for VTM authentication")
parser.add_option("-p", "--password",
                  action="store", dest="passWord",
                  help="password for VTM authentication")


(options, args) = parser.parse_args()

# Do some basic checking of the options
if not ((options.state == 'active') or (options.state == 'disabled') or (options.state == 'draining')):
    sys.exit("State must be one of: active, disabled or draining.")
    

# Set up some variables
headers = {"Content-Type": "application/json"}
url = 'https://'+options.hostName+':9070/api/tm/5.1/config/active/pools/'+options.poolName

# Authenticate and get JSON
requests.packages.urllib3.disable_warnings()
response = requests.get(url,
    headers=headers,
    auth=HTTPBasicAuth(options.userName, options.passWord),
    verify=False)
nodeRef = json.loads(response.text)

# Set status of the node
for item in nodeRef['properties']['basic']['nodes_table']: 
    if item['node'] == options.nodeName:
        item['state'] = options.state
        # Send the modified JSON back
        response = requests.put(
            url,
            headers=headers,
            data=json.dumps(nodeRef).encode("utf-8"),
            auth=HTTPBasicAuth(options.userName, options.passWord),
            verify=False)
        
        if response.status_code != 200:
            print response.status_code, response.reason
