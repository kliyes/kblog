$(document).ready(function(){
	changeImg();
});

var changeImg = function(){
	var $cobj = $("#id_avatar");
	var imgs = new Array();
	$.each( $cobj.find("img") , function( index , val ){
		imgs.push( val );
	} );
	
	var newImg = $(imgs[0]).attr('data-src');
	var ori = $(imgs[0]).attr('src');
	$cobj.hover(function(){
		$(imgs[0]).stop().animate({
			"margin-left":-175
		},300,function(){
			$(imgs[0]).attr('src',newImg);
			$(imgs[0]).stop().animate({
				"margin-left":0				
			},100)
		});
	},function(){
		$(imgs[0]).stop().animate({
			"margin-left":-175
		},100,function(){
			$(imgs[0]).attr('src',ori);
			$(imgs[0]).stop().animate({
				"margin-left":0				
			},300)
		});
	});
}
