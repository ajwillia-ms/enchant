from flask import Flask, abort, session, redirect, render_template

from enchant import model, data
from enchant.server import api


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


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')



@app.route('/login')
def login():
    session['user'] = 'admin'
    return redirect('/')


@app.route('/logout')
def logout():
    session['user'] = None
    return redirect('/')


@app.route('/sites')
def serve_sites():
    return render_template('sites.html', sitelist=data.SITES)


@app.route('/sites/<sitename>/')
def serve_site(sitename):
    site = get_site_or_abort(sitename)

    if len(site.pages) == 0:
        abort(404)
    return render_template('hosted.html', site=site, page=site.pages[0])


@app.route('/sites/<sitename>/<pagename>')
def serve_page(sitename, pagename):
    site = get_site_or_abort(sitename)
    page = get_page_or_abort(site, pagename)

    return render_template('hosted.html', site=site, page=page)

app.secret_key = 'faww3r3jarwc54=c5Y3-543-5avS2'

app.add_url_rule('/api', view_func=api.endpoint)

if __name__ == '__main__':
    app.run()
