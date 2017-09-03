from flask import Flask, abort
from graphene import Enum, List, NonNull, ObjectType, String, Schema
from flask_graphql import GraphQLView

from enchant import model, data

class Query(ObjectType):
    sites = model.ROOT
    def resolve_sites(self, args, context, info):
        return data.SITES

view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query))

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Enchant</h1>\n<p>Enchant is a cloud based CMS for managing multiple web sites quickly and easily.</p>"

@app.route('/sites')
def sitelist():
    content = "<h1>Enchant Sites List</h1><ul>"
    for site in (data.SITES):
        content += "<li><a href=\"/sites/%s\">%s</a> \"%s\"</li>" % (site.name, site.name, site.title)
    content += "</ul>"
    return content

@app.route('/sites/<sitename>')
def site(sitename):
    try:
        site = next(x for x in data.SITES if x.name == sitename)
    except StopIteration:
        abort(404)

    content = "<h1>%s</h1><p>Pages:<ul>" % (site.title)
    for page in (site.pages):
         content += "<li><a href=\"/sites/%s/%s\">%s</a> \"%s\"</li>" % (site.name, page.name, page.name, page.title)
    content += "</ul></p>"
    return content

@app.route('/sites/<sitename>/<pagename>')
def page(sitename, pagename):
    try:
        site = next(x for x in data.SITES if x.name == sitename)
    except StopIteration:
        abort(404)

    try:
        page = next(x for x in site.pages if x.name == pagename)
    except StopIteration:
        abort(404)

    return "<h1>%s :: %s</h1>%s" % (site.title, page.title, page.content)

app.add_url_rule('/api', view_func=view_func)

if __name__ == '__main__':
    app.run()

