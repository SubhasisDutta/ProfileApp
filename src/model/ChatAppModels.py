from google.appengine.ext import ndb

class ChatMessage(ndb.Model):
    """Single Message send by user to chat room"""
    user= ndb.StringProperty(required=True)
    timestamp=ndb.DateTimeProperty(auto_now_add=True)
    message=ndb.TextProperty(required=True)
    def __str__(self):
        return "From %s at %s : %s " %(self.user,self.timestamp,self.message)
    
class ChatTopic(ndb.Model):
    createdBy=ndb.StringProperty(required=True)
    topicName=ndb.StringProperty(required=True)
#     messages = ndb.ListProperty(ChatMessage)