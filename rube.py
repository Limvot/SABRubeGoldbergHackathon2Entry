import subprocess
import time
import base64

import country

subprocess.Popen("python2 shellshock.py", shell=True)
time.sleep(5);
toEncode = "HELLO_WORLD"
toEncode = country.encode(toEncode) 
encoded = None
try:
    encoded = str(subprocess.check_output("curl -m 5 http://localhost/cgi-bin/vulnerable.py?" + toEncode + " || true", shell=True))
except Exception as e:
    print(e)
print("Encoded: ", encoded)
encoded = encoded[3:-2]
print("Encoded: ", encoded)
time.sleep(1);
secret = str(subprocess.check_output("curl http://localhost:8000/srv/http/cgi-bin/secret", shell=True))[2:-3]
print("Secret: ", secret)
time.sleep(1);
encString = bytes.decode(base64.b64decode(encoded))
decString = ""
for i in range(len(encString)):
    decString += chr((ord(encString[i]) ^ ord(secret[i%len(secret)])))
decString = country.decode(decString)
print("Decoded: ", decString)


