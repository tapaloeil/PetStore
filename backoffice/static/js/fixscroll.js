var header = $("#page-header");
  $(window).scroll(function() {
  		if($(window).scrollTop()>=90 && !header.hasClass('fix-header'))
  			header.addClass("fix-header");

  		if($(window).scrollTop()<2 && header.hasClass("fix-header"))
  			header.removeClass("fix-header");
});