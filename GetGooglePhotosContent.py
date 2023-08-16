# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
import requests
import json


# ----------------------------------------------------------------------
# Global Variables
# ----------------------------------------------------------------------
CREDENTIALS_FILE_PATH = 'credentials.json'



# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

def GetOAuthToken(credentialsFilePath):
    credentialsFile = open(credentialsFilePath)
    credentialsFileJson = json.load(credentialsFile)
    OAuthToken = credentialsFileJson['OAuthToken']
    return OAuthToken



# ----------------------------------------------------------------------
# Main Control
# ----------------------------------------------------------------------

# Get the OAuthToken for Google Photos
OAuthToken = GetOAuthToken(CREDENTIALS_FILE_PATH)


print(OAuthToken)
