import webapp2
import os
from google.appengine.ext.webapp import template
from src.model.WorkModels import Work

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/html"
        publishedWork=Work.gql("WHERE publish=True ORDER BY order ")
        template_values = {
                           'pageTitle':"Subhasis Dutta - Profile",
                            'works':publishedWork
                           }
        path=os.path.join(os.path.dirname(__file__),'../../template/index.html')
        page=template.render(path,template_values) 
        self.response.out.write(page)
