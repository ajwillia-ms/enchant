from graphene import Enum, List, NonNull, ObjectType, String, Schema

class PageType(Enum):
    HTML = 1

class Page(ObjectType):
    name = NonNull(String)
    title = NonNull(String)
    content = NonNull(String)
    contenttype = PageType

class Site(ObjectType):
    name = NonNull(String)
    title = NonNull(String)
    pages = List(Page)
    footer = String

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

ROOT = List(Site, description='Enchant Sites')

