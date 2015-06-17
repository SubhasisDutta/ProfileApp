import webapp2
from src.controller.HomeContoller import HomePage
from src.controller.ContactController import ContactModule
from src.controller.SliderController import SliderWS
from src.controller.WorkAdminController import WorkAdminCreate,WorkAdminEdit,AddPhotoTOCollection,MapPhotoToWork,AddWorkAttribute
from src.controller.WorkController import WorkIcon,WorkBigImage,WorkThumbnailPhoto,WorkPhoto,WorkPage

application = webapp2.WSGIApplication([    
    ('/CreateWork',WorkAdminCreate),
    ('/WorkIcon',WorkIcon),
    ('/WorkBigImage',WorkBigImage),
    ('/EditWork',WorkAdminEdit),
    ('/sliderdata',SliderWS),
    ('/AddPhoto',AddPhotoTOCollection),    
    ('/Photo',WorkPhoto),
    ('/Work',WorkPage),
    ('/ContactMessage',ContactModule),
    ('/Thumbnail',WorkThumbnailPhoto),
    ('/MapPhotoToWork',MapPhotoToWork),
    ('/AddAttribute',AddWorkAttribute),
    ('/', HomePage)
], debug=True)

"""def main():
    run_wsgi_app(subhasisapp)
    
if __name__== "__main__":
    main()"""