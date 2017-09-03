from enchant import model

SITES = [model.Site(name='example', title='Example Site',
    pages=[
        model.Page(name='index', title='Welcome',
            content="<p>Welcome, check out the <a href=\"about\">about</a> page.</p>"),
        model.Page(name='about', title='About Us',
            content="<p>Information about us.</p>")
    ])
]

