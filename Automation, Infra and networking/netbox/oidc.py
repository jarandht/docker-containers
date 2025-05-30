# Azure

REMOTE_AUTH_ENABLED = True
SOCIAL_AUTH_AZUREAD_TENANT_OAUTH2_RESOURCE = 'https://graph.microsoft.com'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
REMOTE_AUTH_AUTO_CREATE_USER = True
REMOTE_AUTH_DEFAULT_GROUPS = ["read-only"]

REMOTE_AUTH_BACKEND='social_core.backends.azuread.AzureADOAuth2'
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY=''
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET=''
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# Plain OICD

from os import environ

REMOTE_AUTH_ENABLED = True
REMOTE_AUTH_BACKEND = 'social_core.backends.open_id_connect.OpenIdConnectAuth'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
REMOTE_AUTH_AUTO_CREATE_USER = True

SOCIAL_AUTH_OIDC_OIDC_ENDPOINT = environ.get('SOCIAL_AUTH_OIDC_OIDC_ENDPOINT')
SOCIAL_AUTH_OIDC_KEY = environ.get('SOCIAL_AUTH_OIDC_KEY')
SOCIAL_AUTH_OIDC_SECRET = environ.get('SOCIAL_AUTH_OIDC_SECRET')
SOCIAL_AUTH_OIDC_SCOPE = environ.get('SOCIAL_AUTH_OIDC_SCOPE').split(' ')
LOGOUT_REDIRECT_URL = environ.get('LOGOUT_REDIRECT_URL')


# Bellow is env variables

REMOTE_AUTH_ENABLED = True
REMOTE_AUTH_BACKEND = 'social_core.backends.open_id_connect.OpenIdConnectAuth'
SOCIAL_AUTH_OIDC_OIDC_ENDPOINT = ''
SOCIAL_AUTH_OIDC_KEY = ''
SOCIAL_AUTH_OIDC_SECRET = ''
SOCIAL_AUTH_OIDC_SCOPE=openid profile email roles
LOGOUT_REDIRECT_URL=''
REMOTE_AUTH_AUTO_CREATE_USER = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True