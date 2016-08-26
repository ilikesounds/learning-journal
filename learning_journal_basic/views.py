from pyramid.response import Response
import os


HERE = os.path.dirname(__file__)


def list_view(request):
    imported_text = open(os.path.join(HERE, '/templates/index.html')).read()
    return Response(imported_text)


def detail_view(request):
    imported_text = open(os.path.join(HERE, '/templates/detail.html')).read()
    return Response(imported_text)


def entry_view(request):
    imported_text = open(os.path.join(HERE, '/templates/entry.html')).read()
    return Response(imported_text)


def edit_view(request):
    imported_text = open(os.path.join(HERE, '/templates/edit.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(list_view, route_name='list_view')
    config.add_view(detail_view, route_name='detail_view')
    config.add_view(entry_view, route_name='entry_view')
    config.add_view(edit_view, route_name='edit_view')
