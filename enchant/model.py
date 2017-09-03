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

ROOT = List(Site, description='Enchant Sites')

