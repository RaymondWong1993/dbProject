$(document).ready(function() {
		var category = $('.category');
    var category0 = $('.dropdown-menu');
		var classes = category.find('a');
    var classes0 = category0.find('a');
    classes.each(function() {
				changePage(this);
		});
    classes0.each(function() {
				changePage(this);
		});
});

function changePage(classes) {
    $(classes).click(function() {
				 classes = $(classes).text();
				$.get('/listDisplay/',
							{
									classes: classes
							},
							function (data, status) {
									if (status == 'success') {
                      window.location = '/listDisplay/?='+classes;
									} else {
											alert('get page failed!')
									}
							}
						 );
		});
}
