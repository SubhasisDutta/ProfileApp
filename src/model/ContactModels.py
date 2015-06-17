from google.appengine.ext import ndb

class ContactMessageModel(ndb.Model):
    name=ndb.StringProperty(default="")
    email=ndb.StringProperty(default="")
    message=ndb.TextProperty(default="")