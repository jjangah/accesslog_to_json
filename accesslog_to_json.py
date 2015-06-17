#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import re
import json

# open file : where to read
f = open("filename", 'r')
# open file : where to write
new_f = open("desire_filename", 'w+')

while 1:
	line = f.readline()
	if not line:
		break
	# get values from pattern
	m = re.search( r'(.*) -(.*)- \[(.*)\] \"(.*)\" (.*) (.*) \"(.*)\" \"(.*)\" (.*) (.*) .', line)

	dic={}
	# set access.log attribute and value
	dic['remote_addr'] = m.group(1)
	dic['remote_user'] = m.group(2)
	dic['time_local'] = m.group(3)
	dic['request'] = m.group(4)
	dic['status'] =  m.group(5)
	dic['body_bytes_sent'] = m.group(6)
	dic['http_referer'] = m.group(7)
	dic['http_user_agent'] =  m.group(8)
	dic['request_time'] = m.group(9)
	dic['upstream_response_time'] = m.group(10)

	new_f.write(json.dumps(dic))
	new_f.write("\n")

new_f.close()
f.close()
