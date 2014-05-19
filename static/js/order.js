$(document).ready(function() {
		var orders = $('#orderBox').find('a');
		orders.each(function() {
				$(this).click(function() {
						showContent(this);
				});
		});
});

function showContent(orderInfo) {
		var order = $(orderInfo);
		var orderNum = order.find('#orderNum');
    initialBox();
    orderNum = orderNum.text();
		if (orderNum != '') {
				$.post('/order/',
							 {
									 orderId: orderNum
							 },
							 function(data, status) {
									 if (status == 'success') {
											 $('#orderId').text(data.orderId);
											 $('#orderCustomer').text(data.customer);
											 $('#orderCustomer').parent().css('display', 'block');
											 $('#orderDate').text(data.date);
											 $('#orderDate').parent().css('display', 'block');
											 var orderDetail = data.detail;
											 $.each(orderDetail, function(i, val) {
													 var insertInto = $('.table').find('tbody');
													 html = '<tr><td>'+(i+1)+'</td>'+
															    '<td>'+val['name']+'</td>'+
															    '<td>'+val['count']+'</td>'+
															 '<td>'+val['price']+'</td></tr>';
													 insertInto.append(html);
											 });
											 $('#totalPrice').text(data.totalPrice+'元');
									 } else {
											 alert('Get Order failed!');
									 }
							 }, 'json');
		} else {
				var customerOrderNum = $('#myOrderRestaurant');
				customerOrderNum = customerOrderNum.parent();
				customerOrderNum = customerOrderNum.parent();
				customerOrderNum = customerOrderNum.find('font').text();
				$.post('/order/',
							 {
									 orderId: customerOrderNum
							 },
							 function(data, status) {
									 if (status == 'success') {
											 $('#orderId').text(data.orderId);
											 $('#orderRestaurant').text(data.restaurant);
											 $('#orderRestaurant').parent().css('display', 'block');
											 $('#orderDate').text(data.date);
											 $('#orderDate').parent().css('display', 'block');
											 $('#orderAddress').text(data.address);
											 $('#orderAddress').parent().css('display', 'block');
											 $('#orderPhone').text(data.contact);
											 $('#orderPhone').parent().css('display', 'block');
											 var orderDetail = data.detail;
											 $.each(orderDetail, function(i, val) {
													 var insertInto = $('.table').find('tbody');
													 html = '<tr><td>'+(i+1)+'</td>'+
															    '<td>'+val['name']+'</td>'+
															    '<td>'+val['count']+'</td>'+
															 '<td>'+val['price']+'</td></tr>';
													 insertInto.append(html);
											 });
											 $('#totalPrice').text(data.totalPrice+'元');
									 } else {
											 alert('User Get Order failed!');
									 }
							 }, 'json');
		}
}

function initialBox() {
		$('#orderId').text('');
		$('#orderDate').text('');
		$('#orderCustomer').text('');
		$('#orderRestaurant').text('');
		$('orderAddress').text('');
		$('orderPhone').text('');
		$('.table').find('tbody').empty();
}
