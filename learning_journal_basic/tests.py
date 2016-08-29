import pytest

from pyramid import testing


def test_entry_view():
    from .views import entry_view
    request = testing.DummyRequest()
    info = entry_view(request)
    assert 'entries' in info


def test_detail_view():
    from .views import detail_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = detail_view(request)
    assert 'body' in info


def test_edit_view():
    from .views import edit_view
    request = testing.DummyRequest()
    request.matchdict = {'id': '1'}
    info = edit_view(request)
    assert 'body' in info

# ------- Functional Tests -------


@pytest.fixture()
def testapp():
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'jeff torres' in response.body


def test_root_contents(testapp):
    response = testapp.get('/', status=200)
    assert b'<article>' in response.body
