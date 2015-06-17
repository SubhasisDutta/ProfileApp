import webapp2

from src.model.ContactModels import ContactMessageModel 

class ContactModule(webapp2.RequestHandler):
    def post(self):
        contactPost=ContactMessageModel(name=self.request.get("name"),email=self.request.get("email"),message=self.request.get("message"))
        contactPost.put()
        self.response.headers["Content-Type"]="application/json"
        self.response.out.write("""
                    {
                        "status":"true",
                        "html":"Message has been received." 
                    }
                    """)