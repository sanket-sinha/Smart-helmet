#api: /ZrCUoI7WZE-jNAyhzMFEcA5HLDjQqw58RGGPtCurC

#!/usr/bin/env python
 
import urllib.request
import urllib.parse


def sendSMS(numbers, message):
    params = urllib.parse.urlencode({'apikey': '/ZrCUoI7WZE-jNAyhzMFEcA5HLDjQqw58RGGPtCurC', 'numbers': numbers, 'message': message})
    params = params.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, params)
    return (f.read())


#resp = sendSMS('918697859907', 'My location is: http://maps.google.com/?q=22.5445,84.4612')
#print(resp)
