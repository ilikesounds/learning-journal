"""
Views controller for Pyramid Learning Journal application
"""

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import pytz
from datetime import datetime
from sqlalchemy.exc import DBAPIError
from pyramid.response import Response

from ..models import PLJ_Article


@view_config(route_name='home', renderer='../templates/list.jinja2')
def list_view(request):
    """
    This will return the index page for the Learning Journal
    """
    query = request.dbsession.query(PLJ_Article).order_by(
        PLJ_Article.date_created.desc()
        )
    articles = query.all()
    return {'articles': articles}


@view_config(route_name='detail_view', renderer='templates/detail.jinja2')
def detail_view(request):
    """
    This will return the detail page for an article in the Learning Journal
    """
    try:
        article = request.dbsession.query(PLJ_Article).get(
            request.matchdict['id']
            )
    except DBAPIError:
        return Response(
            db_err_msg,
            content_type='text/plain',
            status=500
            )
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
        new_model = PLJ_Article(
            title=new_title,
            body=new_body,
            date_created=time
            )

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
        time = request.dbsession.query(PLJ_Article).get(
            request.matchdict['id']
            ).date_created
        new_model = PLJ_Article(title=new_title,
                                body=new_body,
                                date_created=time
                                )

        request.dbsession.add(new_model)

        return HTTPFound(request.route_url("home"))
    try:
        article = request.dbsession.query(PLJ_Article).get(
            request.matchdict['id']
            )
    except DBAPIError:
        return Response(db_err_msg,
                        content_type='text/plain',
                        status=500
                        )
    return {'article': article}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:
1.  You may need to run the "initialize_learning_journal_db_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.
2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
After you fix the problem, please restart the Pyramid application to
try it again.
"""
