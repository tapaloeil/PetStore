jQuery(function($) {
	function callServer(source,context){
		var this_=$(source);
		var addURL=this_.attr("data-href");
		qty="{";
		$("input.qty").each(function(index, el) {
			if(el.value>0){
				qty+='"' + el.dataset["cartItemId"] + '":"' + el.value +'",';
			}
		});
		qty = qty.substring(0, qty.length - 1);
		qty+="}";
		console.log(qty);
		$.ajax({
			type: 'GET',
			url: addURL,
			dataType: 'json',
			data: JSON.parse(qty),
			success: function(data){
				if(data["cartItems"]>0){
					if(!$("#cartcount").hasClass('content'))
						$("#cartcount").addClass('content');
					$("#cartcount").html(data["cartItems"])
					$("#cartcount").addClass('shake');
					setTimeout(function (){$("#cartcount").removeClass('shake');}, 2000);
				}
			}
		});
	};

	$("#detail_add_to_cart").click(function(event) {
		callServer(this,"detail");
		$("input.qty").val(0);
	});

	$("#synccart").click(function(event){
		callServer(this,"cart");
		location.reload();
	});

	$(".increment_qty").click(function(event) {
		if(parseInt($(this).siblings("input").val()) < $(this).siblings("input").attr("max") )
			$(this).siblings("input").val(parseInt($(this).siblings("input").val())+1);
	});

	$(".decrement_qty").click(function(event) {
		if(parseInt($(this).siblings("input").val()) > $(this).siblings("input").attr("min") )
			$(this).siblings("input").val(parseInt($(this).siblings("input").val())-1);
	});
});