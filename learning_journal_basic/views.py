"""
Views controller for Pyramid Learning Journal application
"""

from pyramid.view import view_config


ENTRIES = [
    {'title': 'LJ - Test 1', 'creation_date': '08.22.16', 'id': '1', 'body': 'This is text for test entry 1'},
    {'title': 'LJ - Test 2', 'creation_date': '08.23.16', 'id': '2', 'body': 'This is text for test entry 2'},
    {'title': 'LJ - Test 3', 'creation_date': '08.24.16', 'id': '3', 'body': 'This is text for test entry 3'},
]


@view_config(route_name='home', renderer='./templates/index.jinja2')
def list_view(request):
    """
    This will return the index page for the Learning Journal
    """
    return {'entries': ENTRIES}


@view_config(route_name='detail_view', renderer='./templates/detail.jinja2')
def detail_view(request):
    """
    This will return the detail page for an article in the Learning Journal
    """
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry


@view_config(route_name='entry_view', renderer='./templates/entry.jinja2')
def entry_view(request):
    """
    This will return the article entry page for new article in the Learning
    Journal
    """
    return {'entries': ENTRIES}


@view_config(route_name='edit_view', renderer='./templates/edit.html')
def edit_view(request):
    """
    This will return the article edit page for an article in the Learning
    Journal
    """
    for entry in ENTRIES:
        if entry['id'] == int(request.matchdict['id']):
            return entry
