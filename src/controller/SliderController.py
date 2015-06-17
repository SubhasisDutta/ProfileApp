import webapp2

class SliderWS(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"]="application/json"
        sliderData="""[{image : '_include/img/slider-images/image01.jpg', title : '<div class="slide-content">Brushed</div>', thumb : '', url : ''},
                                {image : '_include/img/slider-images/image02.jpg', title : '<div class="slide-content">Brushed</div>', thumb : '', url : ''},
                                {image : '_include/img/slider-images/image03.jpg', title : '<div class="slide-content">Brushed</div>', thumb : '', url : ''},
                                {image : '_include/img/slider-images/image04.jpg', title : '<div class="slide-content">Brushed</div>', thumb : '', url : ''}  
                        ]"""
        self.response.out.write(sliderData)