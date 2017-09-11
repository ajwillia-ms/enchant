from flask import Flask, abort, render_template

from enchant import model, data
from enchant.server import api

def get_site_or_abort(sitename):
    site = model.get_site(data.SITES, sitename)
    if site is None:
        abort(404)
    return site

def get_page_or_abort(site, pagename):
    page = site.get_page(pagename)
    if page is None:
        abort(404)
    return page

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', title='Enchant CMS')

@app.route('/sites')
def sitelist():
    return render_template('sites.html', title='Enchant CMS Sites',
            sitelist = data.SITES)

@app.route('/sites/<sitename>')
def site(sitename):
    site = get_site_or_abort(sitename)

    if len(site.pages) == 0:
        abort(404)
    return render_template('hosted.html', site=site, page=site.pages[0])

@app.route('/sites/<sitename>/<pagename>')
def page(sitename, pagename):
    site = get_site_or_abort(sitename)
    page = get_page_or_abort(site, pagename)

    return render_template('hosted.html', site=site, page=page)

app.add_url_rule('/api', view_func=api.endpoint)

if __name__ == '__main__':
    app.run()

