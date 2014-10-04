#!/bin/python

import subprocess
import threading
import os
import sys
import base64

print("Content-type: text/html\n")

#subprocess.call("date > /tmp/secret", shell=True)
#subprocess.call("/usr/bin/rtl_fm -f 108000 > /tmp/secret", shell=True, timeout = 3)
def doit():
	subprocess.call("rm /tmp/secret", shell=True)
	try:
		#subprocess.call("/usr/bin/rtl_fm -f 108000 > /tmp/secret", shell=True, timeout = 3)
		subprocess.call("/srv/http/cgi-bin/suid_radio", shell=True)
		#print(subprocess.check_output("/usr/bin/rtl_fm -f 108000 &> /tmp/secret", shell=True, timeout = 3))
	except Exception as e:
		pass
		#print("Exception: ", e)

thread = threading.Thread(target=doit)
thread.start()
thread.join(3)
#time.wait(3)
#subprocess.call("


dateStr = str(subprocess.check_output("cat /srv/http/cgi-bin/secret", shell=True))[2:-3]

#strToEncode = "awawefasdf"
strToEncode = os.environ['QUERY_STRING']
#print(strToEncode)
#print("<br>")
encString = ""

#print("<br>Encoded:<br>")
for i in range(len(strToEncode)):
	encString += chr((ord(strToEncode[i]) ^ ord(dateStr[i%len(dateStr)])))
#print(encString)
encBase = base64.b64encode(str.encode(encString))
print(encBase)
#print("PLEASE DIE")
sys.exit()
print("PLEASE DIE")
thread.exit(0)
print("PLEASE DIE")
raise Exception("PLEASE DIE")
print("PLEASE DIE")
sys.exit(0)
print("PLEASE DIE")



decString = ""
#print("<br>Decoded:<br>")
encString = bytes.decode(base64.b64decode(encBase))
for i in range(len(encString)):
	decString += chr((ord(encString[i]) ^ ord(dateStr[i%len(dateStr)])))
#print(decString)

