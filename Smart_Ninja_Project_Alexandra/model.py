from google.appengine.ext import ndb

class Message(ndb.Model):
    message_text = ndb.StringProperty()
    name = ndb.StringProperty()


