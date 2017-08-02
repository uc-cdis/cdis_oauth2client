"""
cdis_oauth2client.oauth2
"""

import flask
import requests

from .exceptions import OAuth2Error


def get_username(user_api=None):
    """
    Given the URL for the user API, call user-api to get the username for the
    current flask session using the current access_token cookie.

    For this function to get the username, the user must already be
    authenticated with an access_token cookie stored in the flask session:

        flask.session['access_token']

    If the `user_api` argument is not provided, get the user API URL from:

        flask.current_app.config['USER_API']

    :param user_api: URL for the user API
    :type user_api: str
    :return: the username:
    :rtype: str
    """
    if user_api is None:
        try:
            user_api = flask.current_app.config['USER_API']
        except KeyError as e:
            raise OAuth2Error("'USER_API' not set in flask.current_app.config")

    try:
        access_token = flask.session['access_token']
    except KeyError:
        code = flask.request.args.get('code')
        if code is None:
            raise OAuth2Error('could not obtain access token')
        access_token = flask.current_app.oauth2.get_access_token(code)

    url = user_api + 'user/'
    headers = {'Authorization': 'Bearer ' + access_token}
    try:
        username = (
            requests.get(url, headers=headers)
            .json()
            .get('username')
        )
    except requests.RequestException as e:
        msg = 'failed to get user info due to requests exception: {}'
        raise OAuth2Error(msg.format(e))
    # TODO: can this except be safely removed? It might be desirable to catch
    # OAuth2Errors resulting from KeyError or RequestException above, which
    # could make this dangerous. Could additionally catch KeyError from the
    # `get(username)` if it is important here to not let most exceptions
    # through.
    except Exception as e:
        msg = 'failed due to unexpected exception: {}'
        raise OAuth2Error(msg.format(e))
    return username
