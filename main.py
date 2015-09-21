import webapp2
from src.controller.HomeContoller import HomePage
from src.controller.ContactController import ContactModule
from src.controller.SliderController import SliderWS
from src.controller.WorkAdminController import WorkAdminCreate,WorkAdminEdit,AddPhotoTOCollection,MapPhotoToWork,AddWorkAttribute
from src.controller.WorkController import WorkIcon,WorkBigImage,WorkThumbnailPhoto,WorkPhoto,WorkPage
# from src.util import SendConfirmationEmailHandler#,SetAnnouncementHandler

application = webapp2.WSGIApplication([    
    ('/admin/CreateWork',WorkAdminCreate),
    ('/WorkIcon',WorkIcon),
    ('/WorkBigImage',WorkBigImage),
    ('/admin/EditWork',WorkAdminEdit),
    ('/sliderdata',SliderWS),
    ('/admin/AddPhoto',AddPhotoTOCollection),    
    ('/Photo',WorkPhoto),
    ('/Work',WorkPage),
    ('/ContactMessage',ContactModule),
    ('/Thumbnail',WorkThumbnailPhoto),
    ('/admin/MapPhotoToWork',MapPhotoToWork),
    ('/admin/AddAttribute',AddWorkAttribute),
#     ('/crons/set_announcement', SetAnnouncementHandler),
#     ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/profile',HomePage)    
], debug=True)

"""def main():
    run_wsgi_app(subhasisapp)
    
if __name__== "__main__":
    main()"""