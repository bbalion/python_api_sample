#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
import swiftclient
import user_config
import url_config
import pprint

base_url=url_config.storage_url
accesskey=user_config.accesskey
storagesecret=user_config.storagesecret


swift = swiftclient.client.Connection( user=accesskey, key=storagesecret, authurl=base_url)
# Create container
container_name='container1'
object_name=''

headers = {'X-Container-Read': '.r:*'}
swift.post_container(container_name, headers)

# List containers
pprint.pprint(swift.head_account(), width=1)

# List objects in the container 
pprint.pprint(swift.head_container(container_name), width=1)
