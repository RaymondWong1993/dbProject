$(document).ready(function() {
    window.type = 1;
		var userBtn = $('#userBtn');
    var restaurantBtn = $('#restaurantBtn');
    var submitBtn = $('#submitBtn');
    userBtn.click(function() {
        window.type = 1;
        changeContent(1);
    });
    restaurantBtn.click(function() {
        window.type = 2;
        changeContent(2);
    });
    submitBtn.click(function() {
        submit(window.type);
    });
});

function changeContent(avaliable) {
    if (avaliable == 1 && $('#userBox').css('display') == 'none') {
        var showBox = $('#userBox');
        var hiddenBox = $('#restaurantBox');
        hiddenBox.fadeToggle('fast', function() {
            showBox.fadeToggle('fast');
            $('.modal-content-custom').css('height','400px');
        });
    } else if (avaliable == 2 && $('#restaurantBox').css('display') == 'none') {
        var showBox = $('#restaurantBox');
        var hiddenBox = $('#userBox');
        hiddenBox.fadeToggle('fast', function() {
            showBox.fadeToggle('fast');
            $('.modal-content-custom').css('height','500px');
        });
    }
    //howBox.fadeToggle();//('display', 'block');
    //hiddenBox.fadeToggle();//('display', 'none');
}

function submit(avaliable) {
    var userBtn = $('#userBtn');
    var restaurantBtn = $('#restaurantBtn');
    var data_ = {};
    if (avaliable == 1) {
        var phone = $('#userBox').find('#phone').val();
        var email = $('#userBox').find('#email').val();
        var password = $('#userBox').find('#password').val();
        data_['contact'] = phone;
        data_['username'] = email;
        data_['hashpw'] = password;
				data_['type'] = 'yummy_user';
    } else {
        var name = $('#restaurantBox').find('#name').val();
        var address = $('#restaurantBox').find('#address').val();
        var contact = $('#restaurantBox').find('#contact').val();
        var account = $('#restaurantBox').find('#account').val();
        var password = $('#restaurantBox').find('#password').val();
        data_['name'] = name;
        data_['address'] = address;
        data_['username'] = account;
        data_['hashpw'] = password;
				data_['contact'] = contact;
				data_['type'] = 'yummy_business';
    }
    $.post('/register/',
          data_,
          function(data,status) {
							if (status == 'success') {
									if (data.resp == 1) {
											window.location = '/home/';
									} else {
											alert('1注册失败！');
											window.location = '/register/';
									}
							} else {
									alert('2注册失败！');
							}
          });
}
