$('ul').on('click', ':checkbox', function() {
	$(this).parent().toggleClass('completed');
});

$('ul').on('click', 'span', function() {
	$(this).parent().fadeOut(200, function() {
		$(this).remove();
	});
});

$("input[type='text']").keypress(function(event) {
	if (event.which === 13) {
		var item = $(this).val();
		$(this).val('');
		$('ul').append('<li><input type="checkbox">' + item + ' <span><i class="fas fa-trash"></i></span></li>');
	}
});

let newItemOpen = true;

$('.newItemToggle').click(function() {
	$("input[type='text']").fadeToggle();
	if (newItemOpen) {
		$(this).removeClass('fa-minus').addClass('fa-plus');
		newItemOpen = false;
		console.log('closed');
	} else {
		$(this).removeClass('fa-plus').addClass('fa-minus');
		newItemOpen = true;
		console.log('opoened');
	}
});
