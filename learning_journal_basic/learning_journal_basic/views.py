from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def my_view(request):
    imported_text = open(os.path.join(HERE, 'sample.txt')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(my_view, route_name='home')
