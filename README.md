##### Google Tag Manager Python API integrated with Analytics API

This project is using both [Google Tag Manager API](https://developers.google.com/tag-manager/api/v1/devguide) and [Google Analytics API](https://developers.google.com/analytics/devguides/config/mgmt/v3/quickstart/installed-py).
Create javascript snippet code for your Google Tag Manager by providing your Site Name, Site URL. This service will connect to your Google Analytics account to create a new web property for your account based on Site Name and Site URL command line params. After creating web property, it will get web property's tracking code to feed it into Google Tag Manager.
This project creates [Universal Analytics](https://support.google.com/analytics/answer/2790010?hl=en) Tag
<br/>
<br/>
##### Warning from Google Analytics API docs
```
Write operations in the Management API (e.g. create, update, delete, patch) for Web Property,
View (Profile), and Goal resources are currently available as a developer preview in limited beta.
If you're interested in using these features, request access to the beta.
```
Please create a project on [Google Developer Console](https://console.developers.google.com/flows/enableapi?apiid=analytics&credential=client_key) and apply to [request access to beta](https://docs.google.com/forms/d/e/1FAIpQLSf01NWo9R-SOHLKDUH0U4gWHNDBIY-gEI-zqBMG1Hyh3_hHZw/viewform) before creating a web property to get tracking code.

<br/>

##### Enable required APIs
[Enable Google Tag Manager API](https://console.developers.google.com/start/api?id=tagmanager&credential=client_key)

[Enable Google Analytics API](https://console.developers.google.com/flows/enableapi?apiid=analytics&credential=client_key)

<br/>

##### Make required changes in settings.py

```python
 #enable/disable sending javascript code snippet in email.
SEND_CODE_SNIPPET_EMAIL = True

# SMPT settings goes here...

# secret key must be in /secrets/ folder. otherwise change directory here
# How to get secret key JSON file. Follow link
# https://developers.google.com/tag-manager/api/v1/devguide#environment

GOOGLE_DEVELOPER_SECRET_KEY = os.path.join('secrets', 'google_developer_secret.json')

TIME_ZONE_COUNTRY_ID = 'US'
TIME_ZONE_ID = 'America/Los_Angeles'

# possible values: web, android, ios
GOOGLE_TAG_USAGE_CONTEXT = ['web']
```

<br/>
##### Switch to project root directory and Install dependencies from requirements.txt file
```
pip install -r requirements.txt
```

<br/>
##### What command do i need to execute?
```
# simply run from the command line
python index.py --site_name MY_SITE_NAME --site_url MY_SITE_URL
```

<br/>
##### What do you get?
![Google Tag Manager Preview](http://i.imgur.com/uzeDj0b.png)

<br/>
##### Tested Environment
```
Python 2.7
Python 3.4
Google Tag Manager API Version 1
Google Analytics API Version 3
Ubuntu 14.04
```
