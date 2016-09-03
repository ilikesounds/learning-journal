# -*- coding utf-8 -*-
from webtest import TestApp as _TestApp
import pytest


@pytest.fixture()
def app():
    settings = {'sqlalchemy.url': 'sqlite db path'}
    my_app = main({}, **settings)
    app = _Test_App(my_app)
    return app
