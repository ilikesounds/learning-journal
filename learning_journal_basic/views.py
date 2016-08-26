from pyramid.view import view_config
import os


HERE = os.path.dirname(__file__)


@view_config(route_name='list_view', renderer='')
def list_view(request):
    imported_text = open(os.path.join(HERE, './templates/index.html')).read()
    return Response(imported_text)


@view_config(route_name='detail_view', renderer='')
def detail_view(request):
    imported_text = open(os.path.join(HERE, './templates/detail.html')).read()
    return Response(imported_text)


@view_config(route_name='entry_view', renderer='')
def entry_view(request):
    imported_text = open(os.path.join(HERE, './templates/entry.html')).read()
    return Response(imported_text)


@view_config(route_name='edit_view', renderer='')
def edit_view(request):
    imported_text = open(os.path.join(HERE, './templates/edit.html')).read()
    return Response(imported_text)
