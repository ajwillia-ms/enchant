from graphene import Enum, List, NonNull, ObjectType, String, Schema

class PageType(Enum):
    HTML = 1

class Page(ObjectType):
    name = NonNull(String)
    title = NonNull(String)
    contenttype = PageType
    content = String

    def __init__(self, name, title, contenttype):
        self.name = name
        self.title = title
        self.contenttype = contenttype
        self.content = ''

class HTMLPage(Page):

    def __init__(self, name, title, content):
        super(HTMLPage, self).__init__(name, title, PageType.HTML)
        self.content = content

class Site(ObjectType):
    name = NonNull(String)
    title = NonNull(String)
    pages = List(Page)
    footer = String

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.pages = []

    def get_page(self, pagename):
        try:
            return next(x for x in self.pages if x.name == pagename)
        except StopIteration:
            return None

def get_site(sitelist, sitename):
    try:
        return next(x for x in sitelist if x.name == sitename)
    except StopIteration:
        return None

