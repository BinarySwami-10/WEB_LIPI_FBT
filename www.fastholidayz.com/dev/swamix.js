import "https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.1.3/js/bootstrap.bundle.min.js"
import "https://cdnjs.cloudflare.com/ajax/libs/Swiper/7.4.1/swiper-bundle.min.js"
/*--------------------*/
print = console.log

/*--------------------*/
function smoothScrollWindow () {
	$(document).ready(function() {
		$("a[href^='#']").on('click', function(e) {
			e.preventDefault();
			var hash = this.hash;
			$('html, body').animate({
				scrollTop: $(hash).offset().top }, 1000,
				function(){window.location.hash = hash;
				});
		});
	});
}
setTimeout(smoothScrollWindow, 2500)
/*--------------------*/

/*--------------------*/
function void_data_loader () {
	 $('[data-load]').each(function(index, el) {
		$.get($(el).attr('data-load'), function(data) {
			$(el).html(data)
		});
	});
}


/*--------------------*/
function template_generator (parentSelector){
	parent = $(parentSelector)
	child_template = parent.children().first().remove().html()
}
/*--------------------*/
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}


/*--------------------DOCUMENT READY TRIGGERS*/
$(document).ready(function() {
	$('.row').addClass('mx-0')
	void_data_loader()
});