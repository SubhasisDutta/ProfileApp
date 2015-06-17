import webapp2
import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import ndb
from google.appengine.api import images

from src.model.WorkModels import Work,PhotoModel,WorkResourceAttribute

class WorkAdminCreate(webapp2.RequestHandler):
    #create project page render
    def get(self):
        user=users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers["Content-Type"]="text/html"
            admins=['subhasisdutta300887','subhasistubai','test@example.com']
            if user.nickname() not in admins:
                self.response.out.write(callAccessDeniedPage())
            else:
                template_values={
                         'pageTitle':"Create New Work Project",                                                 
                         }
                path=os.path.join(os.path.dirname(__file__),'../../template/createWork.html')
                page=template.render(path,template_values) 
                self.response.out.write(page) 
            
    #create project post
    def post(self):
        handle=self.request.get("handle")
        category=self.request.get("category")
        title=self.request.get("title")
        description=self.request.get("description")
        icon=self.request.get("iconImage")
        largeImage=self.request.get("largeImage")
        iconImg=db.Blob(icon)
        largeImg=db.Blob(largeImage)
        workItem=Work(id=handle)        
        workItem.category=category
        workItem.title=title
        workItem.order=int(self.request.get("order"))
        workItem.description=description
        workItem.iconImage=iconImg
        workItem.bigImage=largeImg
        workItem.put()
        self.response.headers["Content-Type"]="text/html"
        self.response.out.write("""
                    <html>
                    <head>
                    <title>New WORK Created</title>
                    </head>
                    <body>
                    <h3> New WORK Created</h3>
                    </body></html>
                    """)
        

class WorkAdminEdit(webapp2.RequestHandler):
    #display the 3 form controller to get 
    def get(self):
        user=users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers["Content-Type"]="text/html"
            admins=['subhasisdutta300887','subhasistubai','test@example.com']
            if user.nickname() not in admins:
                self.response.out.write(callAccessDeniedPage())
            else:
                work_name=self.request.get("name")
                work_key=ndb.Key('Work',work_name)
                work=work_key.get()
                if work is None:
                    self.response.out.write(callNoSuchWorkPage())
                else:
                    attrList=ndb.get_multi(work.attributes)
                    photoList=ndb.get_multi(work.photoGallery)
                    template_values={
                                     'pageTitle':"Edit Work",
                                     'work':work,
                                     'attrList': attrList,
                                     'photoList': photoList                                        
                                    }
                    path=os.path.join(os.path.dirname(__file__),'../../template/editWork.html')
                    page=template.render(path,template_values) 
                    self.response.out.write(page)

    def post(self):
        user=users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers["Content-Type"]="text/html"
            admins=['subhasisdutta300887','subhasistubai','test@example.com']
            if user.nickname() not in admins:
                self.response.out.write(callAccessDeniedPage())
            else:
                work_name=self.request.get("name")
                work_key=ndb.Key('Work',work_name)
                work=work_key.get()
                if work is None:
                    self.response.out.write(callNoSuchWorkPage())
                else:                    
                    title=self.request.get("title")
                    description=self.request.get("description")                                                      
                    work.title=title
                    work.description=description   
                    work.order=int(self.request.get("order"))
                    work.publish=bool(self.request.get("publish"))                 
                    work.put()
                    self.response.headers["Content-Type"]="text/html"
                    self.response.out.write("""
                    <html>
                    <head>
                    <title>Project main Updated</title>
                    </head>
                    <body>
                    <h3> Project main Updated</h3>
                    </body></html>
                    """)

class AddWorkAttribute(webapp2.RequestHandler):
    def post(self):        
        attribute=WorkResourceAttribute(name=self.request.get("name"),htmlDescription=self.request.get("htmlDescription"),order=int(self.request.get("order")))
        attribute.put()
        work_key=ndb.Key('Work',self.request.get("workHandle"))
        work=work_key.get()
        work.attributes.append(attribute.key)
        work.put()
        self.response.headers["Content-Type"]="text/html"
        self.response.out.write("""
                    <html>
                    <head>
                    <title>New Attribute Added</title>
                    </head>
                    <body>
                    <h3> New Attribute Added</h3>
                    </body></html>
                    """)

class AddPhotoTOCollection(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers["Content-Type"]="text/html"
            admins=['subhasisdutta300887','subhasistubai','test@example.com']
            if user.nickname() not in admins:
                self.response.out.write(callAccessDeniedPage())
            else:
                template_values={
                         'pageTitle':"Create New Photo",                                                 
                         }
                path=os.path.join(os.path.dirname(__file__),'../../template/createPhoto.html')
                page=template.render(path,template_values) 
                self.response.out.write(page)               
    def post(self):
        photoImage=self.request.get("image")
        photoImg=db.Blob(photoImage)
        thumbnail=images.resize(photoImage, 250, 170)
        thumbnailImg=db.Blob(thumbnail)
        photo=PhotoModel(title=self.request.get("title"),image=photoImg,type=self.request.get("type"),thumbnail=thumbnailImg,caption=self.request.get("caption"))      
        photo.put()
        self.response.headers["Content-Type"]="text/html"
        self.response.out.write("""
                    <html>
                    <head>
                    <title>Photo Added</title>
                    </head>
                    <body>
                    <h3> New Photo Added</h3>
                    </body></html>
                    """)  
          
class MapPhotoToWork(webapp2.RequestHandler):
    def get(self):
        user=users.get_current_user()
        if user is None:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            self.response.headers["Content-Type"]="text/html"
            admins=['subhasisdutta300887','subhasistubai','test@example.com']
            if user.nickname() not in admins:
                self.response.out.write(callAccessDeniedPage())
            else:
                work_name=self.request.get("name")
                work_key=ndb.Key('Work',work_name)
                work=work_key.get()
                if work is None:
                    self.response.out.write(callNoSuchWorkPage())
                else:
                    attrList=ndb.get_multi(work.attributes)
                    photoList=ndb.get_multi(work.photoGallery)
                    photoCollection= PhotoModel.query()
                    template_values={
                                          'pageTitle':"Map Photo To Work : ",
                                          'work':work,
                                          'attrList': attrList,
                                          'photoList': photoList,
                                          'photoCollection': photoCollection                                       
                                          }
                    path=os.path.join(os.path.dirname(__file__),'../../template/mapPhotoWork.html')
                    page=template.render(path,template_values) 
                    self.response.out.write(page)
    def post(self):  
        workPhoto_key=ndb.Key(urlsafe=self.request.get("photoKey"))    
        work_key=ndb.Key('Work',self.request.get("name"))
        work=work_key.get()
        work.photoGallery.append(workPhoto_key)
        work.put()
        self.response.headers["Content-Type"]="text/html"
        self.response.out.write("""
                    <html>
                    <head>
                    <title>New Photo Added</title>
                    </head>
                    <body>
                    <h3> New Photo Added</h3>
                    </body></html>                    
                    """)
        
def callNoSuchWorkPage():
    template_parameters={
                 'pageTitle':'No Such Work!!!!',
                 'title':"ERROR! Requested Work cannot be found",                                 
                 'message':"ERROR!! The requested work was not found. Please check the name again."
                   }
    error_template=os.path.join(os.path.dirname(__file__),'../../template/error.html')
    page=template.render(error_template,template_parameters) 
    return page

def callAccessDeniedPage():
    template_parameters={
                    'pageTitle':'Access Denied!!!!',
                    'title':"ERROR! You don't have access to this page",                                 
                    'message':"ERROR!! You don't have access to this page."
                   }
    error_template=os.path.join(os.path.dirname(__file__),'../../template/error.html')
    page=template.render(error_template,template_parameters) 
    return page