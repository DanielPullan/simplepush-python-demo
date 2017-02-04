# i had to pip-install simplepush, if you have issues, installing python-dev
# fixed it for me
from simplepush import send_encrypted
# i made a config file defining key, password and salt so that I could upload
# it once and then gitignore it to avoid encryption keys being uploaded
from config import *


# make calling push use simplepush to send a notification to phone
push = send_encrypted (key, password, salt, "title", "message", "event")

# make a value to have a number to go True or False against
number = 4563

# if the number isn't equal to 1, call our push event
if number != 1:
        push
# else,print "don't push" as a way of knowing the value returned False
else:
        print ("don't push")
