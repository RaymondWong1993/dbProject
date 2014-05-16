$(document).ready(function() {
	var signInBtn = $("#signInBtn");
	var logoutBtn = $("#logoutBtn");
	var userLoginBtn = $('#userLoginBtn');
	var restaurantLoginBtn = $('#restaurantLoginBtn');
	window.type = 1;
	//checkLogIn();
	signInBtn.click(function() {
		signIn(window.type);
	});
	logoutBtn.click(function() {
		logout();
	});
	userLoginBtn.click(function() {
		window.type = 1;
		userLogin();
  });
  restaurantLoginBtn.click(function() {
		window.type = 2;
		restaurantLogin();
  });
})

function checkLogIn() {
    show = ['logoutBtn'];
    hide = ['signInBoxBtn', 'registerBtn'];
    if (typeof $.cookie('user') != 'undefined' && typeof $.cookie('type' != 'undefined')) {
        if ($.cookie('type') == 'customer') {
						show.push('myAccountBtn');
        } else {
						show.push('myRestaurantBtn');
				}
        changeBtn(show, hide);
    } else {
        changeBtn(hide, show);
    }
}

function signIn(avaliable) {
	emailTag = $("#email");
	passwdTag = $("#passwd");
	email = emailTag.val();
	passwd = passwdTag.val();
	if (email == '' || passwd == '') {
		alert('登录失败!')
		return;
	}
	show = ['logoutBtn'];
	hide = ['registerBtn', 'signInBoxBtn'];
		account = $('#account').val();
		if (avaliable == 1) {
		    $.post('/login',
              {
					    		'email': email,
                  'password': passwd,
                  'type': 'customer',
              });
        show.push('myAccountBtn');
        changeBtn(show, hide);
    } else {
        $.post('/login',
              {
					    		'account': account,
                  'password': passwd,
                  'type': 'restaurant',
              });
        show.push('myRestaurantBtn');
        changeBtn(show, hide);
    }
}

function changeBtn(show, hide) {
    $.each(show, function(i, val) {
        $('#'+val).css('display', 'block');
    });
    $.each(hide, function(i, val) {
				$('#'+val).css('display', 'none')
    });
}

function logout() {
	$("#registerBtn").css("display", "block");
	$("#signInBoxBtn").css("display", "block");
	$('#myRestaurantBtn').css("display","none");
	$("#myAccountBtn").css("display", "none");
	$("#logoutBtn").css("display", "none");
	// $.cookie('user', null, { expires: -1});
	// $.cookie('type', null, { expires: -1});
}

function userLogin() {
		var showbox = $('#userLogin');
    var hiddenbox = $('#restaurantLogin');
    showbox.css('display','block');
    hiddenbox.css('display','none');
}

function restaurantLogin() {
		var showbox = $('#restaurantLogin');
    var hiddenbox = $('#userLogin');
    showbox.css('display','block');
    hiddenbox.css('display','none');
}
