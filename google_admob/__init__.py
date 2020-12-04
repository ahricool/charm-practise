import os

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

...

# Authenticate using the client_secrets file.
client_secrets = os.path.join(
    os.path.dirname(__file__), 'client_secret.json')
flow = Flow.from_client_secrets_file(
    client_secrets,
    scopes=['https://www.googleapis.com/auth/adsense.readonly'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# Redirect the user to auth_url on your platform.
auth_url, _ = flow.authorization_url()
print('Please go to this URL: {}\n'.format(auth_url))

# The user will get an authorization code. This code is used to get the
# access token.
code = input('Enter the authorization code: ')
flow.fetch_token(code=code)
credentials = flow.credentials

print(credentials)


admob = build('admob', 'v1', credentials=credentials)

# Get AdMob account information by replacing publisher_id,
# which follows the format "pub-XXXXXXXXXXXXXXXX".
# See https://support.google.com/admob/answer/2784578
# for instructions on how to find your publisher ID.
result = admob.accounts().list().execute()

# Print the result.
print(result)