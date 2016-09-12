"""
Views controller for Pyramid Learning Journal application
"""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
import pytz
from datetime import datetime

from ..models import PLJ_Article

@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """
    This will return the index page for the Learning Journal
    """
    articles = request.dbsession.query(PLJ_Article).order_by(PLJ_Article.date_created.desc())
    article = articles.all()
    return {'articles': article}


@view_config(route_name='detail_view', renderer='templates/detail.jinja2')
def detail_view(request):
    """
    This will return the detail page for an article in the Learning Journal
    """
    try:
        article = request.dbsession.query(PLJ_Article).get(request.matchdict['id'])
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'article': article}


@view_config(route_name='entry_view', renderer='../templates/entry.jinja2')
def entry_view(request):
    """
    This will return the article entry page for new article in the Learning
    Journal
    """
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        time = datetime.now(pytz.utc)
        new_model = PLJ_Article(title=new_title, body=new_body, date_created=time)

        request.dbsession.add(new_model)

        return HTTPFound(request.route_url("home"))

    return {}


@view_config(route_name='edit_view', renderer='templates/edit.jinja2')
def edit_view(request):
    """
    This will return the article edit page for an article in the Learning
    Journal
    """
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        time = datetime.now(pytz.utc)
        new_model = PLJ_Article(title=new_title, body=new_body, date_created=time)

        request.dbsession.add(new_model)

        return HTTPFound(request.route_url("home"))
    try:
        article = request.dbsession.query(PLJ_Article).get(request.matchdict['id'])
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'article': article}
