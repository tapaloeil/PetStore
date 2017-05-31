jQuery(function($) {

	function selectCarouselImage(iid){
		$("#image-preview").attr("src",$("#"+iid).attr("src"));
		$(".wrapper>img").css("border","0");
		$("#"+iid).css("border","2px solid #00BCD4");
	}
	function startCarousel(){
		$(".wrapper>img").click(function(event) {
			selectCarouselImage(this.id);
		});
		selectCarouselImage($("#carousel .wrapper img")[0].id);
	}

	if($("#carousel > img").length>0){
		$( "#carousel" ).rcarousel( {
			width: 100, 
			height: 100,
			step: 1,
			visible:$("#carousel > img").length,
			orientation:"horizontal",
			start: startCarousel
		});
	}
	else
		$(".gallery").css("display","none");
});