import os

RECEIVER_EMAIL = 'CODE_SNIPPET_RECIEVER_EMAIL_ADDRESS'
SENDER_EMAIL = 'no-reply@gmail.com'
EMAIL_SUBJECT = 'Google Tag Manager Code Snippet'

# enable/disable sending javascript code snippet in email
SEND_CODE_SNIPPET_EMAIL = True

# SMTP server credentials
SMTP_EMAIL = ''  # example.gmail.com
SMTP_PASSWORD = ''  # ksj*)9900sdf
SMTP_HOST = ''  # smtp.gmail.com
SMTP_PORT = ''  # 587

# enable/disable error traceback
DUBUG = False

# secret key must be in /secrets/ folder. otherwise change directory here
# How to get secret key JSON file. Follow link
# https://developers.google.com/tag-manager/api/v1/devguide#environment

GOOGLE_DEVELOPER_SECRET_KEY = os.path.join('secrets', 'google_developer_secret.json')


TIME_ZONE_COUNTRY_ID = 'US'
TIME_ZONE_ID = 'America/Los_Angeles'

# possible values: web, android, ios
GOOGLE_TAG_USAGE_CONTEXT = ['web']

