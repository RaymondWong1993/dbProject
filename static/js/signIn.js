$(document).ready(function() {
	var signInBtn = $("#signInBtn");
	var logoutBtn = $("#logoutBtn");
	signInBtn.click(function() {
			signIn();
	});
	logoutBtn.click(function() {
		logout();
	});
})

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
