import pytest

from pyramid import testing


def test_detail_view():
    from .views import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    assert "title" in info

# ------- Functional Tests -------

@pytest.fixture()
def testapp():
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)

def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'This is text for test entry' in response.body

def test_root_contents(testapp):
    response = testapp.get('/', status=200)
    assert b'<article>' in response.body
