from pyramid.security import Allow
from pyramid.security import Everyone, Authenticated
from passlib.apps import custom_app_context as password_context
import os


class Root(object):
    def __init__(self, request):
        self.request = request

    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'root')
    ]


def verify_user(username, password):
    is_user_authenticated = False
    env_username = os.environ.get('PLJ_USER')
    env_password = os.environ.get('PLJ_PASS')
    if env_username and env_password:
        if username == env_username:
            try:
                is_user_authenticated = password_context.verify(
                    password,
                    env_password
                    )
            except ValueError:
                pass

    return is_user_authenticated
