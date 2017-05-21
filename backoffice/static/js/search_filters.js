function buildFilterMenu(item){
	if(item[0]!=""){
		$(".filter-add > li[data-filter-dest='"+ item[0] +"'][data-text='"+item[1]+"']").children("a").removeClass("amshopby-attr");
		$(".filter-add > li[data-filter-dest='"+ item[0] +"'][data-text='"+item[1]+"']").children("a").addClass("amshopby-attr-selected");

		$("#resetFilterButton").css("display","block");
	}
}

function getJsonFromUrl(query) {
  var result = {};
  query.split("&").forEach(function(part) {
    var item = part.split("=");
    buildFilterMenu(item);
    result[item[0]] = decodeURIComponent(item[1]);
  });
}

$(document).ready(function() {
    $("#resetFilterButton").click(function(event) {
        $("#q").val("");
        $("#SearchForm").submit();
    });
	getJsonFromUrl($("#q").val());
	$('.amsopby-flag-clickfirst > li').click(function(event) {
		var dataset = $(this)[0].dataset;
		if($(this).children("a").hasClass('amshopby-attr')){
			$("#q").val($("#q").val() + dataset.filterDest + "=" + dataset.text + "&");
		}
		if($(this).children("a").hasClass('amshopby-attr-selected')){
			var str = dataset.filterDest + "=" + dataset.text + "&";
			$("#q").val($("#q").val().replace(str,""));
		}
		$("#SearchForm").submit();
	});
});