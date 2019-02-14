$("ul").on("click", ":checkbox", function(){
	$(this).parent().toggleClass("completed");
});

$("ul").on("click", "span", function(){
	$(this).parent().fadeOut(200, function(){
		$(this).remove();
	})
});

$("input[type='text']").keypress(function(event){
	if(event.which === 13) {
		var item = $(this).val();
		$(this).val("");
		$("ul").append('<li><input type="checkbox">' + item + ' <span><i class="fas fa-trash"></i></span></li>');
	}
});

$(".fa-plus").click(function() {
	$("input[type='text']").fadeToggle();
});