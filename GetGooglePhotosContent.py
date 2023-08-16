# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
import os
import pickle
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

# ----------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# API Variables
# ----------------------------------------------------------------------
API_SERVICE_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

# ----------------------------------------------------------------------
# Main Control
# ----------------------------------------------------------------------

# Get Credentials from the credential file and start local server
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
cred = flow.run_local_server()

# Start service
google_photos = build(API_SERVICE_NAME, API_VERSION, credentials=cred, static_discovery=False)
print(API_SERVICE_NAME, 'Service Created Successfully!')

# Create a csv file to hold the output
outFile = open("out.csv", "w")

# List all media item names
count = 0
nextpagetoken = 'Dummy'
while nextpagetoken != '':
    nextpagetoken = '' if nextpagetoken == 'Dummy' else nextpagetoken
    results = google_photos.mediaItems().search(body={"pageSize": 10, "pageToken": nextpagetoken}).execute()
    items = results.get('mediaItems', [])
    nextpagetoken = results.get('nextPageToken', '')
    for item in items:
        fileString = str(item['filename']) + "," + str(item['mimeType']) + "," + str(item['mediaMetadata']['creationTime'])
        outFile.writelines(fileString + '\n')
        count = count + 1
        print(str(count) + " / " + fileString)


