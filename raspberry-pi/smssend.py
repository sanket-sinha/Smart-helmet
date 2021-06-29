

#!/usr/bin/env python
 
import urllib.request
import urllib.parse
apikey= "<apikey>"

def sendSMS(numbers, message):
    params = urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers, 'message': message})
    params = params.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, params)
    return (f.read())


