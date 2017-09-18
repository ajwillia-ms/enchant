from flask import Flask, abort, render_template
from graphene import ObjectType, Schema
from flask_graphql import GraphQLView

from enchant import model, data


def get_site_or_abort(sitename):
    ret = model.get_site(data.SITES, sitename)
    if ret is None:
        abort(404)
    return ret


def get_page_or_abort(site, pagename):
    ret = site.get_page(pagename)
    if ret is None:
        abort(404)
    return ret


class Query(ObjectType):
    sites = model.ROOT

    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def resolve_sites(self, args, context, info):
        return data.SITES


view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/sites')
def serve_sites():
    return render_template('sites.html', sitelist=data.SITES)


@app.route('/sites/<sitename>/')
def serve_site(sitename):
    site = get_site_or_abort(sitename)

    return render_template('hosted.html', site=site, page=site.pages[0])


@app.route('/sites/<sitename>/<pagename>')
def serve_page(sitename, pagename):
    site = get_site_or_abort(sitename)
    page = get_page_or_abort(site, pagename)

    return render_template('hosted.html', site=site, page=page)


app.add_url_rule('/api', view_func=view_func)

if __name__ == '__main__':
    app.run()
