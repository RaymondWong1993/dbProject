$(document).ready(function() {
	var submitBtn = $('#submitBtn');
	window.food = [];
	window.count = [];
	window.price = [];
	var confirmBtn = $('#confirm');
	var cancelBtn = $('#cancel');
	//checkLogin();
	submitBtn.click(function() {
        getOrder();
	});
	confirmBtn.click(function() {
		confirmOrder();
	});
	cancelBtn.click(function() {
		cancelOrder();
	});
})

function getOrder() {
	var li = $('#list').children();
    li.each(function() {
        var input = $(this).find('input');
        if ($(input[0]).prop('checked')) {
        	window.food.push($(this).find('h4').text());
        	if ($(input[1]).val() == '') {
        		window.count.push(1);
        	} else {
        		window.count.push($(input[1]).val());
        	}
        	window.price.push(parseInt($(this).find('p.price').text()) * parseInt(count[count.length - 1]));
        }
    });
    showOrder();
}

function showOrder() {
	var counter = 1
	var len = window.food.length;
	var insertInto = $('.table').find('tbody');
	var html = '';
	var totalPrice = 0;
	while (counter <= len) {
        html = '<tr><td>'+counter+'</td>'+
               '<td>'+window.food[counter - 1]+'</td>'+
               '<td>'+window.count[counter - 1]+'</td>'+
               '<td>'+window.price[counter - 1]+'</td></tr>';
        insertInto.append(html);
        totalPrice = totalPrice + parseInt(window.price[counter - 1]);
		counter = counter + 1;
	}
	$('#totalPrice').text(totalPrice+'元');
	window.food = [];
	window.count = [];
	window.price = [];
}

function confirmOder() {
	$('.table').find('tbody').empty();
	$.post('/restaurantDetail/',
		   {
		   	food: window.food,
		   	count: window.count,
		   	price: window.price
		   },
		   function(data) {
		   	if (data.status == 'success') {
		   		alert('post order success!');
		   	} else {
		   		alert('post order failed!');
		   	}
		   });
}

function cancelOrder() {
	$('.table').find('tbody').empty();
}
