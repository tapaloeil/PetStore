jQuery(function($) {
	$("#detail_add_to_cart").click(function(event) {
		var this_=$(this);
		var addURL=this_.attr("data-href");
		//qtyArray=JSON.parse('{"items":[]}');
		qty="{";
		$("input.qty").each(function(index, el) {
			if(el.value>0){
				qty+='"' + el.dataset["cartItemId"] + '":"' + el.value +'",';
				//qtyArray["items"].push('{"' + el.dataset["cartItemId"] + '","' + el.value +'"}');
			}
		});
		qty = qty.substring(0, qty.length - 1);
		qty+="}";
		$.ajax({
			type: 'GET',
			url: addURL,
			dataType: 'json',
			data: JSON.parse(qty),
			success: function(data){
				console.log(data);
				$("#cartcount").html(data["cartItems"])
			}
		});
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