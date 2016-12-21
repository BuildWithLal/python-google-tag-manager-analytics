"""
Access and manage a Google Tag Manager account.
"""
from __future__ import print_function, unicode_literals
import sys
import os
import re

from utils import Email
from google_tag_manager_api import *
from google_analytics_api import GetOrCreateTrackingId, GetService as GetAnalyticsService
import settings
import validators


def main(argv):
    """
    Get tag manager account ID, Site Name and Google Analytics Tracking ID from command line.
    Account ID as a string input to create a Tag for. Site name for creating container to get javascript code snippet.
    Google Analytics tracking id, where you want get all type of tracking
    """

    sys.tracebacklimit = settings.DUBUG

    args_help = """
    Site Name, Site URL and Google Analytics Tracking ID from command line.
    Site name and Site URL for creating container to get javascript code snippet.
    Google Analytics tracking id, where you want get all type of tracking
    """

    parser = argparse.ArgumentParser(description=args_help)
    parser.add_argument('--site_name', type=str, help='Your site name', required=True)
    parser.add_argument('--site_url', type=str, help='Your site URL', required=True)
    args = parser.parse_args()

    container_name = str(args.site_name)
    container_site = str(args.site_url)

    if not validators.url(container_site):
        raise Exception('invalid site URL')

    # Define the auth scopes to request.
    tag_manager_scope = ['https://www.googleapis.com/auth/tagmanager.edit.containers',
             'https://www.googleapis.com/auth/tagmanager.edit.containerversions',
             'https://www.googleapis.com/auth/tagmanager.publish'
             ]

    # Define the auth scopes to request.
    analytics_scope = ['https://www.googleapis.com/auth/analytics.edit']

    # Authenticate and construct service.
    analytics_service = GetAnalyticsService('analytics', 'v3', analytics_scope, settings.GOOGLE_DEVELOPER_SECRET_KEY)
    tracking_id = GetOrCreateTrackingId(analytics_service, container_name, container_site)

    # Authenticate and construct service.
    tag_manager_service = GetService('tagmanager', 'v1', tag_manager_scope, settings.GOOGLE_DEVELOPER_SECRET_KEY)

    account_id = GetAccountID(tag_manager_service)

    # get container id to create tag
    container_id = CreateOrGetContainer(tag_manager_service, account_id, container_name, container_site)

    # Create the hello world tag for tracking id
    CreateOrGetTag(tag_manager_service, account_id, container_id, tracking_id)

    container_version_id = CreateContainerVersion(tag_manager_service, account_id, container_id)

    PublishContainerVersion(tag_manager_service, account_id, container_id, container_version_id)

    container_public_id = CreateOrGetContainer(tag_manager_service, account_id, container_name, container_site, 'public_id')

    print('Preparing javascript code snippet...')

    with open(os.path.join('code_snippet', 'gtm_backup.txt'), 'r') as gtm:
        gtm_snippet = gtm.read()
        gtm.close()

    with open(os.path.join('code_snippet', 'gtm.txt'), 'w') as gtm:
        gtm_snippet = re.sub(r'XXXXXXXX', container_public_id, gtm_snippet)
        gtm.write(gtm_snippet)
        gtm.close()

    print(gtm_snippet)

    if settings.SEND_CODE_SNIPPET_EMAIL:
        Email.send()


if __name__ == '__main__':
    main(sys.argv)
