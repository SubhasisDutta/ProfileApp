import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

from src.model.WorkModels import Work

class WorkIcon(webapp2.RequestHandler):
    def get(self):
        work_key=ndb.Key('Work',self.request.get("key"))
        work=work_key.get()
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(work.iconImage)

class WorkBigImage(webapp2.RequestHandler):
    def get(self):
        actualKey=self.request.get("key").replace('.jpg','')
        work_key=ndb.Key('Work',actualKey)
        work=work_key.get()
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(work.bigImage)
        
class WorkThumbnailPhoto(webapp2.RequestHandler):
    def get(self):
        workPhoto_key=ndb.Key(urlsafe=self.request.get("key"))
        workPhoto=workPhoto_key.get()
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(workPhoto.thumbnail)

class WorkPhoto(webapp2.RequestHandler):
    def get(self):
        workPhoto_key=ndb.Key(urlsafe=self.request.get("key"))
        workPhoto=workPhoto_key.get()
        self.response.headers['Content-Type'] = 'image/jpeg'
        self.response.out.write(workPhoto.image)
        
class WorkPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="text/html"
        work_key=ndb.Key('Work',self.request.get("name",default_value=None))
        work=work_key.get()
        if work is None:             
            self.response.out.write(callNoSuchWorkPage())
        else:
            attrList=ndb.get_multi(work.attributes)
            photoList=ndb.get_multi(work.photoGallery)
            template_values={
                            'pageTitle': work.title,
                            'work':work,
                            'attrList': attrList,
                            'photoList': photoList                                        
                           }
            path=os.path.join(os.path.dirname(__file__),'../../template/workView.html')
            page=template.render(path,template_values) 
            self.response.out.write(page)
            
def callNoSuchWorkPage():
    template_parameters={
                         'pageTitle':'No Such Work!!!!',
                         'title':"ERROR! Requested Work cannot be found",                                 
                         'message':"ERROR!! The requested work was not found. Please check the name again."
                        }
    error_template=os.path.join(os.path.dirname(__file__),'../../template/error.html')
    page=template.render(error_template,template_parameters) 
    return page
