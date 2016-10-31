import pytest
import pytz
from datetime import datetime
import transaction
from pyramid import testing
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session
)
from ..models.mymodel import PLJ_Article
from ..models.meta import Base
import os


# ---------- Fixtures for tests ---------------

@pytest.fixture(scope='session')
def db_engine(request):
    config = testing.setUp(settings={
        'sqlalchemy.url': 'sqlite:///:memory:'
    })
    config.include('..models')
    settings = config.get_settings()
    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    def teardown():
        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope='function')
def test_session(db_engine, request):
    session_factory = get_session_factory(db_engine)
    dbsession = get_tm_session(session_factory, transaction.manager)

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return dbsession


@pytest.fixture(scope='function')
def dummy_http_request(test_session):
    """
    This is a generic dummy GET request generator
    """
    test_request = testing.DummyRequest()
    test_request.dbsession = test_session
    return test_request


def dummy_http_request_post(title, body, new_session):
    """
    This is a generic dummy POST request generator
    """
    test_request = testing.DummyRequest()
    test_request.dbsession = new_session
    test_request.method = 'POST'
    test_request.POST['title'] = title
    test_request.POST['body'] = body
    test_request.POST['date_created'] = datetime.now(pytz.utc)
    return test_request

# ------- DB tests --------------


def test_model_added(test_session):
    """Test the creation of the new model."""
    assert len(test_session.query(PLJ_Article).all()) == 0
    time = datetime.now(pytz.utc)
    model = PLJ_Article(title="entry",
                        body="body",
                        date_created=time
                        )
    test_session.add(model)
    test_session.flush()
    assert len(test_session.query(PLJ_Article).all()) == 1

# ----------- View tests ------------


def test_get_list_view_title(test_session):
    """Test whether list_view returns correct title from DB"""
    from ..views.default import list_view
    time = datetime.now(pytz.utc)
    model = PLJ_Article(title="test_title",
                        body="test_body",
                        date_created=time
                        )
    test_session.add(model)
    test_session.flush()
    result = list_view(dummy_http_request(test_session))
    assert result['articles'][0].title == 'test_title'


def test_get_list_view_body(test_session):
    """Test whether list_view returns correct body from DB"""
    from ..views.default import list_view
    time = datetime.now(pytz.utc)
    model = PLJ_Article(title="test_title",
                        body="test_body",
                        date_created=time
                        )
    test_session.add(model)
    test_session.flush()
    result = list_view(dummy_http_request(test_session))
    assert result['articles'][0].body == 'test_body'


def test_get_detail_view(test_session):
    """Test detail_view is correctly returned"""
    from ..views.default import detail_view
    time = datetime.now(pytz.utc)
    model = PLJ_Article(title="test_title",
                        body="test_body",
                        date_created=time
                        )
    test_session.add(model)
    test_session.flush()
    request = dummy_http_request(test_session)
    request.matchdict['id'] = 1
    result = detail_view(request)
    assert result['article'].title == 'test_title'


def test_get_edit_view(test_session):
    """
    Test edit_view is correctly returned
    """
    from ..views.default import edit_view
    time = datetime.now(pytz.utc)
    model = PLJ_Article(title="test_title",
                        body="",
                        date_created=time
                        )
    test_session.add(model)
    test_session.flush()
    request = dummy_http_request(test_session)
    request.matchdict['id'] = 1
    result = edit_view(request)
    assert result['article'].title == 'test_title'


def test_entry_view_error_message(test_session):
    """
    Test that an error message is returned on no characters in title or body
    """
    from ..views.default import entry_view
    result = entry_view(dummy_http_request_post('', '', test_session))
    import pdb; pdb.set_trace()
    assert result['error_message'] == '''You must enter at least one character in the Title and Body fields.'''
