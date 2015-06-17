$(document).ready(function(){
	var noofpics=$(".photoGalleryBox #scroller ul li").length;
	
	if ($.browser.msie) {
		//alert( $.browser.version );
		//$(".photoGalleryBox #scroller ul").niceScroll();	
		$(".photoGalleryBox #scroller ul").css("{overflow: scroll;}");
	}
	else{
		$(".photoGalleryBox #scroller").width(noofpics*280);
		var myScroll = new iScroll('wrapper', { hScrollbar: false, vScrollbar: false ,vScroll:false});
	}
	$(".photoGalleryBox .popupPicture").click(function(event) {		
		var title=$(this).siblings("img").attr("title");
		var caption=$(this).siblings("img").attr("caption");
		var urlsafe=$(this).siblings("img").attr("urlsafe");		
		var imagePopupTemplate="<div class='projectImagePopup'>" +
									"<img src='/ProjectPhoto?key=~urlsafe~' alt'~title~' title='~title~'/>" +
									"<div class='imageDescriptionBox'>" +
										"<div class='imageTitle'>~title~</div>" +
										"<div class='imageCaption'>~caption~</div>" +
									"</div>" +
								"</div>";
		var imageHtml=imagePopupTemplate.replace(/~title~/g,title).replace("~caption~",caption).replace("~urlsafe~",urlsafe);
		$("#middleEmptyBox .ChatContentBox").html(imageHtml);
		$("#middleEmptyBox").bPopup({
			fadeSpeed: 'slow',
            followSpeed: 1500
		});
	});
});