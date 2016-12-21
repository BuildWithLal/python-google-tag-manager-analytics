#### [Google Tag Manager Python API integrated with Analytics API](https://developers.google.com/tag-manager/api/v1/devguide)

Create javascript snippet code for your Google Tag Manager by providing your Site Name, Site URL. This service will connect to your Google Analytics account to create a new web property for your account based on Site Name and Site URL command line params. After creating web property, it will get web property's tracking code to feed it into Google Tag Manager.
This project creates [Universal Analytics](https://support.google.com/analytics/answer/2790010?hl=en) Tag

##### Make required changes in settings.py
```python
# enable/disable sending javascript code snippet in email.
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

##### Switch to project root directory and Install dependencies from requirements.txt file
```
pip install -r requirements.txt
```

##### What command do i need to execute?
```
# simply run from the command line
python index.py --site_name MY_SITE_NAME --site_url MY_SITE_URL
```

##### What do you get?
![Google Tag Manager Preview](https://lh3.googleusercontent.com/QFJ_RJin-qM0gRnuM-Q2lfiqqscBqC7oiHI7hlIcMiVHFP-SVSUYF5U9SL2fGYXzCQXuZPodPeEdtdlJRc-0nrcSeZaQYwXGGlWoRZP0olGNjC5-vJOyvgktnqoLf4dga3ZcoZeYLs4U0dCaZv8qn2a9Qb-3647QGLBt5g_Ujeeb32bEQo6Ni_vKE83GYWlflwZC0DxJ4tbnY8Amg3WhMVxcgBSatbGL3dnk2OGZ5fWE5pSmEGbasgs54VLpWY5R80HtQrX1iOeTBruUpsWl3xeCoZiA4mEiPtXO-QR8E-f2CCndRDJvhc_kqmS-nx9ZZG8e3cUWowfbtUOHd7yNbqXZeEN4VAVBWb39wkfn4bStLNuUUpNrl-6KGbgKSqWwqj3SiEz0EpPOYAZEIxPqYNInnIVSQDnflTWE7DnhrUza0q3IDSrBiZrndrfX6BPlhyU_ee8VLAN0yPltYWsci07JOFSLRK6ZaCEKVry3h7YC7o8eR6bBIia9Yr-gqUqykjg7wpEqRN-jKTNfhjsgxzq-_HIQi61YShewgmKbPVRC-R3rmj6XhhLbOic8QCATW3YYqDcGKzTc_asOHFkfbxjEwdACyvOXOmVsEhDRnGtPK-fvj1mf=w1084-h581-no)

##### Tested Environment
```
Python 2.7
Python 3.4
Google Tag Manager API Version 1
Google Analytics API Version 3
Ubuntu 14.04
```
