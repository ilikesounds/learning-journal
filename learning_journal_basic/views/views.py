"""
Views controller for Pyramid Learning Journal application
"""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
import datetime

from ..models import PLJ_Article

@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """
    This will return the index page for the Learning Journal
    """
    query = request.dbsession.query(PLJ_Article).order_by(PLJ_Article.date_created.desc())
    entries = query.all()
    return {'entries': entries}


@view_config(route_name='detail_view', renderer='templates/detail.jinja2')
def detail_view(request):
    """
    This will return the detail page for an article in the Learning Journal
    """
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry


@view_config(route_name='entry_view', renderer='../templates/entry.jinja2')
def entry_view(request):
    """
    This will return the article entry page for new article in the Learning
    Journal
    """
    return {}


@view_config(route_name='edit_view', renderer='templates/edit.jinja2')
def edit_view(request):
    """
    This will return the article edit page for an article in the Learning
    Journal
    """
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry
