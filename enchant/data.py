from enchant import model

example = model.Site(name='example', title='Example Site')
example.pages=[
        model.HTMLPage(name='index', title='Welcome',
            content="<p>Welcome, check out the <a href=\"about\">about</a> page.</p>"),
        model.HTMLPage(name='about', title='About Us',
            content="<p>Information about us.</p>")
    ]
example.footer='footer text'

SITES = [example,]

