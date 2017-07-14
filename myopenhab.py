

import sys
import json
import requests
import time
import urlparse
import sys


def batteryLevel( level ):
    "This returns a string value for a battery level"
    l = 'empty'

    try:
        v = float(level)
    except:
        v = 0

    if (v < 5):
        l = 'empty'
    elif (v < 20):
        l = 'low'
    elif (v < 90):
        l = 'medium'
    elif (v < 100):
        l = 'high'
    else:
        l = 'full'

    return l


def mapValues(k, map):
    v = "unkown"
    if(str(k) in map):
        v = map[str(k)]
    return v


def getJSONValue(obj, path):
	pathOK = True
	subObj = obj
	v = ""
	try:
		for k in path:
			if(isinstance(k, basestring)):
				if(str(k) in subObj):
					subObj = subObj[k]
					v = subObj
				else:
					pathOK = False
					break
			else:
				subObj = subObj[k]
				v = subObj
	except:
		pathOK = False

	if (pathOK):
		return v
	else:
		return None


class openhab(object):
    """
    A wrapper for the OpenHab REST API.

    """

    def __init__(self):

    	self.openhab_ip = "10.0.1.102:8080"
      
    def sendCommand(self, item, state):
        """
        Update State from Item
        """

        try:
        	if (isinstance(state, basestring)):
        	    r = requests.put('http://' + str(self.openhab_ip) + '/rest/items/' + item + '/state', state.encode('utf-8'))
        	else:
        	    r = requests.put('http://' + str(self.openhab_ip) + '/rest/items/' + item + '/state', str(state))        	    	

	        if(r.status_code == 202):
	        	print "Successfully posted state to OpenHab: " + str(item)
	        else:
	        	print "Error posting state to OpenHab: " + str(item) + " (HTTP Response " + str(r.status_code) + ")"
        except:
            print "OpenHab: Error posting state:" + str(sys.exc_info()[1])


    def getState(self, item):
        """
        Get State for Item
        """

        try:
        	r = requests.get('http://' + str(self.openhab_ip) + '/rest/items/' + item + '/state')
	        if(r.status_code == 200):
	        	print "Successfully got state from OpenHab: " + str(item)
	        	state = str(r.content)
	        	if (state == ""): state = "NULL"
		        return state
	        else:
	        	print "Error getting state from OpenHab: " + str(item) + " (HTTP Response " + str(r.status_code) + ")"
		        return ""
        except:
            print "OpenHab: Error getting state:" + str(sys.exc_info()[1])





