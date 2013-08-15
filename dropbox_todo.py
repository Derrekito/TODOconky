import cmd
import locale
import os
import os.path
import pprint
import shlex

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website
APP_KEY = ''
APP_SECRET = ''

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

access_token = ''
auth_token = ''
sess.set_token(access_token, auth_token)

# Sign other API calls is to pass the session object to DropboxClient
client = client.DropboxClient(sess)

# Download a file
f= client.get_file('/TODO.txt').read()
file = f
pad = f.split('\n')
list = []
for i in range(len(pad)-1):
    if pad[i][0] != 'x':
        list.append(pad[i])

for i in range(len(list)): #take blank line into account
    if len(list[i])> 30:
        s = list[i].splitlines(10) # careful, is string is long enough this will break
        for i in range(len(s)):
            print s[i]
    else:
        print list[i]



