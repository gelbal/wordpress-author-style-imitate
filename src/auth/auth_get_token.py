import sys
import os
import requests
import urllib.parse

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.utils.helper import load_env

load_env()

AUTHORIZATION_BASE_URL = 'https://public-api.wordpress.com/oauth2/authorize'
TOKEN_URL = 'https://public-api.wordpress.com/oauth2/token'
CLIENT_ID = <CLIENT_ID>
CLIENT_SECRET = <CLIENT_SECRET>
REDIRECT_URI = <REDIRECT_URI>

SCOPES = [
    'posts',  # Read and write posts
    'comments',  # Read and write comments
    'taxonomy',  # Read and write tags and categories
    'stats', # Grants access to site statistics
]

# Step 1: Get the authorization URL
auth_params = {
    'client_id': CLIENT_ID,
    'redirect_uri': REDIRECT_URI,
    'response_type': 'code',
    'blog': 'data.blog',
    'scope': ' '.join(SCOPES)
}
authorization_url = f"{AUTHORIZATION_BASE_URL}?{urllib.parse.urlencode(auth_params)}"

print(f'Please go to this URL and authorize the application: {authorization_url}')

# Step 2: Get the authorization code from the redirect URL
redirect_response = input('Enter the full redirect URL: ')

# Extract the authorization code from the redirect URL
parsed_url = urllib.parse.urlparse(redirect_response)
code = urllib.parse.parse_qs(parsed_url.query)['code'][0]

# Step 3: Exchange the code for an access token
token_params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': code,
    'grant_type': 'authorization_code',
    'redirect_uri': REDIRECT_URI
}

print(f"Token params: {token_params}")

response = requests.post(TOKEN_URL, data=token_params)

if response.status_code == 200:
    token_data = response.json()
    print(f"Access token: {token_data['access_token']}")
    print(f"Refresh token: {token_data.get('refresh_token', 'No refresh token provided')}")
    print(f"Full response: {token_data}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")
