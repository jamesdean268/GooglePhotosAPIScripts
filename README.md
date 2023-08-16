# GooglePhotosAPIScripts
Scripts to supprt querying the Google Photos API

## Setup
Install the requirements to run the python scripts

``` 
python -m pip install -r requirements.txt 
```

Create a Google OAuth2 Token set following the guide here: https://developers.google.com/photos/library/guides/get-started
Download the OAuth Client JSON file from the Google Cloud console, and paste the contents into a file called "credentials.json" in the root directory

## Execution
Execute the Python script to list items within Google Photos

``` 
python GetGooglePhotosContent.py 
```
