"""
cdis_oauth2client.blueprint

Provides a Flask blueprint for authorization.

Exports:
    ``blueprint``
        A Flask blueprint which provides the following endpoints:
        * ``/authorization_url``
              returns the authorization url for the current app's OAuth2Client
        * ``/authorize``
              authorize a user using the ``authorize`` function provided from
              cdis_oauth2client.oauth2
        * ``/logout``
              log out a user by clearing the flask session
"""

import flask
from flask import current_app

from .oauth2 import authorize


blueprint = flask.Blueprint('oauth', 'oauth_v0')


@blueprint.route('/authorization_url', methods=['GET'])
def get_authorization_url():
    """Just return the authorization URL (from the client)."""
    return current_app.oauth2.authorization_url


@blueprint.route('/authorize', methods=['GET'])
def do_authorize():
    """
    Call ``authorize`` to authorize the user (authorize returns the username)
    and store the username in the Flask session.
    """
    flask.session['username'] = authorize(
        current_app.oauth2,
        current_app.config['USER_API'],
        flask.request.args.get('code')
    )
    return ''


@blueprint.route('/logout', methods=['GET'])
def logout_oauth():
    """
    Log out the user by clearing the Flask session (thus removing the
    username from the session).
    """
    flask.session.clear()
    return ''
