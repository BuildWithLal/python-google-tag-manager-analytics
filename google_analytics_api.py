"""
Access Google Analytics API and create or get web property tracking ID
"""
from __future__ import print_function, unicode_literals
from googleapiclient.discovery import build

import httplib2
import settings
from googleapiclient.http import HttpError
import simplejson as json
from oauth2client import client
from oauth2client import file
from oauth2client import tools
import argparse


def GetService(api_name, api_version, scope, client_secrets_path):
  """
  Get a service that communicates to a Google API.

  Args:
    api_name: string The name of the api to connect to.
    api_version: string The api version to connect to.
    scope: A list of strings representing the auth scopes to authorize for the
      connection.
    client_secrets_path: string A path to a valid client secrets file.

  Returns:
    A service that is connected to the specified API.
  """

  print('Connecting to Google Analytics service...')

  # Parse command-line arguments.
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawDescriptionHelpFormatter,
      parents=[tools.argparser])
  flags = parser.parse_args([])

  # Set up a Flow object to be used if we need to authenticate.
  flow = client.flow_from_clientsecrets(
      client_secrets_path, scope=scope,
      message=tools.message_if_missing(client_secrets_path))

  # Prepare credentials, and authorize HTTP object with them.
  # If the credentials don't exist or are invalid run through the native client
  # flow. The Storage object will ensure that if successful the good
  # credentials will get written back to a file.
  storage = file.Storage(api_name + '.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, flags)
  http = credentials.authorize(http=httplib2.Http())

  # Build the service object.
  service = build(api_name, api_version, http=http)

  return service


def GetOrCreateTrackingId(service, site_name, site_url):

    print('Creating Web property to get Tracking ID...')

    accounts = service.management().accounts().list(fields='items').execute()

    if accounts.get('items'):

        # Get the first Google Analytics account.
        account = accounts.get('items')[0].get('id')

        # Get a list of all the properties for the first account.
        properties = service.management().webproperties().list(accountId=account, fields='items').execute()

        if properties.get('items'):

          # check if property already exists then simply return tracking code from property
          for property in properties.get('items'):
              if site_name == property.get('name'):
                  return property.get('id')

          try:
              web_property = service.management().webproperties().insert(
                  accountId=account,
                  fields='id',
                  body={
                      'websiteUrl': site_url,
                      'name': site_name
                  }
              ).execute()

          except TypeError as error:
              # Handle errors in constructing a query.
              raise Exception('There was an error in constructing your query : %s' % error)

          except HttpError as error:
              # Handle API errors.
              raise Exception('There was an in API call or your Account ID. Original Message: %s :' % (json.loads(error.content)['error']['message']))

    return web_property.get('id')
