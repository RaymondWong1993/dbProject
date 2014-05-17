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
    if (avaliable == 1) {
        var showBox = $('#userBox');
        var hiddenBox = $('#restaurantBox');
        hiddenBox.fadeToggle('fast', function() {
            showBox.fadeToggle('fast');
            $('.modal-content-custom').css('height','400px');
        });
    } else {
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
        var phone = $('#phone').val();
        var email = $('#email').val();
        var password = $('#password').val();
        data_['phone'] = phone;
        data_['username'] = email;
        data_['password'] = password;
    } else {
        var name = $('#name').val();
        var address = $('#address').val();
        var contact = $('#contact').val();
        var account = $('#account').val();
        var password = $('#password').val();
        data_['name'] = name;
        data_['address'] = contact;
        data_['username'] = account;
        data_['password'] = password;
        data_['contact'] = contact;
    }
    $.post('/register',
          data_,
          function(data,status) {
              alert(status);
          });
}
