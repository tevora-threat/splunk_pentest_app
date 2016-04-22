import splunk.entity as entity
import splunk.auth, splunk.search
import getpass

def huntPasswords(sessionKey):
    entities = entity.getEntities(
            ['admin','passwords'],owner="nobody", namespace="-",sessionKey=sessionKey)
    return entities

def getSessionKeyFromCreds():
    user = raw_input("Username:")
    password = getpass.getpass()
    sessionKey = splunk.auth.getSessionKey(user,password)
    return sessionKey

if __name__ == "__main__":
    sessionKey = getSessionKeyFromCreds()
    print huntPasswords(sessionKey)
