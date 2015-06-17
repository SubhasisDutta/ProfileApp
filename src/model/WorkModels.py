from google.appengine.ext import ndb


class WorkResourceAttribute(ndb.Model):
    name=ndb.StringProperty(required=True)
    htmlDescription=ndb.TextProperty(default="")
    order=ndb.IntegerProperty(required=True)
    
class PhotoModel(ndb.Model):
    image=ndb.BlobProperty()
    thumbnail=ndb.BlobProperty()
    title=ndb.StringProperty(required=True)
    caption=ndb.StringProperty()
    type=ndb.StringProperty(required=True)

class Work(ndb.Model):    
    creationTimestamp=ndb.DateTimeProperty(auto_now_add=True)
    category=ndb.StringProperty(required=True)
    title=ndb.StringProperty(required=True)
    description=ndb.TextProperty(required=True)
    iconImage=ndb.BlobProperty(required=True)
    bigImage=ndb.BlobProperty(required=True)
    order=ndb.IntegerProperty(required=True)
    publish=ndb.BooleanProperty(default=False)
    attributes=ndb.KeyProperty(repeated=True)
    photoGallery=ndb.KeyProperty(repeated=True)    

    