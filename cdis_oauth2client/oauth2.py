"""
cdis_oauth2client.oauth2

Provides :py:func:``authorize`` to perform the OAuth2 authorization. Note that
this module should be kept entirely Flask-agnostic, i.e. Flask should not be
imported here and :py:func:``authorize`` should accept an ``OAuth2Client`` with
a ``get_token`` method, in order to modularize the logic.
"""

import requests

from .exceptions import OAuth2Error


def authorize(oauth_client, user_api, code):
    """
    Authorize an OAuth client.

    :param oauth_client: the OAuth2 client to authorize
    :type oauth_client: OAuth2Client
    :param user_api: URL for the user API
    :type user_api: str
    :param code: will usually be flask.request.args.get('code')
    :type code: str
    :return: the username
    :rtype: str
    """
    if not code:
        raise OAuth2Error('no authorization code provided')

    token_response = oauth_client.get_token(code)
    access_token = token_response.get('access_token')
    if not access_token:
        raise OAuth2Error(
            message='did not receive access token in response from client',
            json=token_response
        )

    try:
        headers = {'Authorization': 'Bearer ' + access_token}
        request = requests.get(user_api + 'user/', headers=headers)
        user_api_response = request.json()
    except requests.RequestException as e:
        raise OAuth2Error(
            'failed to get user info due to requests exception: {}'.format(e)
        )
    except Exception as e:
        raise OAuth2Error('failed due to unexpected exception: {}'.format(e))

    username = user_api_response.get('username')
    if not username:
        raise OAuth2Error(json=user_api_response)
    return username
