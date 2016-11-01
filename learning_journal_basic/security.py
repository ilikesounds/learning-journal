from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
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
    env_username = 'j'
    env_password = '$6$rounds=637725$VjGuGRrTDTlXEAKK$dHlQHIwnJgIQ/qSmuerapBLFgznz6WWn.Cfq.ioMsMxbkUSQczYG5jXXiD2NsNjnfBx37Ej0/oP4YXy81aoNr.'
    if env_username and env_password:
        if username == env_username:
            try:
                is_user_authenticated = password_context.verify(
                    password,
                    env_password
                    )
                return is_user_authenticated
            except ValueError:
                pass

    return is_user_authenticated


def includeme(config):
    """security-related configuration"""
    os.environ['PLJ_AUTH_SECRET'] = password_context.encrypt(
        'ThisPasswordIsSecret'
        )
    auth_secret = os.environ.get('PLJ_AUTH_SECRET', '')
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg='sha512'
    )

    authz_policy = ACLAuthorizationPolicy()

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_default_permission('view')
    config.set_root_factory(Root)
