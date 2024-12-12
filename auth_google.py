import json
import requests
from google_auth_oauthlib.flow import Flow
from kivy.utils import platform

# Constants
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['openid', 'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile']


def login_with_google():
    # Custom OAuth redirect URI for mobile
    if platform == 'android':
        redirect_uri = "com.example.app:/oauth2redirect"
    elif platform == 'ios':
        redirect_uri = "yourapp:/oauth2redirect"
    else:
        redirect_uri = "http://localhost:8080"

    # Initialize the flow with the redirect URI
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=redirect_uri
    )

    # Get the authorization URL
    auth_url, _ = flow.authorization_url(prompt='consent')

    # Direct the user to login in an external browser
    if platform in ['android', 'ios']:
        from kivy.utils import platform
        import webbrowser
        webbrowser.open(auth_url)
    else:
        print("Open this URL in your browser: ", auth_url)

    # Wait for redirect and handle it
    # For mobile, we need a method to listen to redirects.
    # This can be done using WebView-based redirection on Android/iOS with additional configurations.
    # flow.fetch_token(authorization_response=redirect_response)

    # After getting the token
    credentials = flow.credentials
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {credentials.token}'})
    user_info = session.get('https://www.googleapis.com/userinfo/v2/me').json()

    return user_info
