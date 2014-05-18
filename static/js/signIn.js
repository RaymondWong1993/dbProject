$(document).ready(function() {
	var signInBtn = $("#signInBtn");
	var logoutBtn = $("#logoutBtn");
		var detailBtns = $('.detailBtn');
	signInBtn.click(function() {
			signIn();
	});
	logoutBtn.click(function() {
		logout();
	});
		detailBtns.each(function() {
				$(this).click(function() {
						turnPage(this);
				});
		});
})

function turnPage(btn) {
    var restaurantName = $(btn).parent();
    restaurantName = restaurantName.parent();
		restaurantName = restaurantName.find('h2');
		restaurantName = restaurantName.text();
		$.get('/restaurantDetail/',
					{
							'name': restaurantName
					},
					function(data, status) {
							if (status == 'success') {
									window.location = '/restaurantDetail/?name=' + restaurantName;
							} else {
									alert('餐厅详情打开失败！');
							}
					});
}

function signIn() {
		emailTag = $("#email");
		passwdTag = $("#passwd");
		email = emailTag.val();
		passwd = passwdTag.val();
		$.post('/login/',
					 {
							 'username': email,
							 'hashpw': passwd,
					 }, function(data, status) {
							 if (status == 'success') {
									 if (data.resp == 0) {
											 emailTag.val('');
											 passwdTag.val('');
											 alert('登录失败！');
									 } else
											 window.location = '/home/';
							 } else {
									 emailTag.val('');
									 passwdTag.val('');
									 alert('登录失败！');
							 }
					 });
}

function logout() {
	$("#registerBtn").css("display", "block");
	$("#signInBoxBtn").css("display", "block");
	$('#myRestaurantBtn').css("display","none");
	$("#myAccountBtn").css("display", "none");
	$("#logoutBtn").css("display", "none");
}
