# i had to pip-install simplepush, if you have issues, installing python-dev
# fixed it for me
from simplepush import send_encrypted
# imported requests in order to have something to play with
import requests
# i made a config file defining key, password and salt so that I could upload
# it once and then gitignore it to avoid encryption keys being uploaded
from config import *

# make different pushes to send a notification to phone with simplepush
push = send_encrypted (key, password, salt, "title", "message", "event")
downAlert = send_encrypted (key, password, salt, "Website", "Server is down")
upAlert = send_encrypted (key, password, salt, "Website", "Server is up")
# prod the bee's nest and see what happens
response = requests.get('http://danielpullan.co.uk')

# print the resulting mess
print(int(response.status_code))

# response 200 means all is well
if response.status_code == 200:
    # so announce all is well
    print "website up"
    upAlert
# else it isn't
else:
    #so announce that all is not well
    print "website down"
    downAlert
