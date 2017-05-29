jQuery(function($) {
	$("#detail_add_to_cart").click(function(event) {
		$("input.qty").each(function(index, el) {
			if(el.value>0){
				$.ajax({
				  url: "http://localhost:8090/fr/cart/add/"+ el.dataset["cartItemId"] +"/1/",
				  context: document.body
				}).done(function() {
				  console.log( "done" );
				});
			}
		});
		$("input.qty").val(0);
	});

	$(".increment_qty").click(function(event) {
		if(parseInt($(this).siblings("input").val()) < $(this).siblings("input").attr("max") )
			$(this).siblings("input").val(parseInt($(this).siblings("input").val())+1);
	});

	$(".decrement_qty").click(function(event) {
		if(parseInt($(this).siblings("input").val()) > $(this).siblings("input").attr("min") )
			$(this).siblings("input").val(parseInt($(this).siblings("input").val())-1);
	});

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