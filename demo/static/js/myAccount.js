$(document).ready(function() {
	var selfIntroductionBtn = $("#selfIntroductionBtn");
    var shoppingHistoryBtn = $("#shoppingHistoryBtn");
    var myOrderBtn = $('#myOrderBtn');
    var creditBtn = $('#myCreditBtn');
    changeBtn();
    selfIntroductionBtn.click(function() {
        pageTurning(1);
    });
    shoppingHistoryBtn.click(function() {
        pageTurning(4);
    });
    myOrderBtn.click(function() {
        pageTurning(2);
    });
    creditBtn.click(function() {
        pageTurning(3);
    });
})

function changeBtn() {
    $('#registerBtn').css('display', 'none');
    $('#signInBoxBtn').css('display', 'none');
    $('#myAccountBtn').css('display', 'block');
    $('#logoutBtn').css('display', 'block');
}

function pageTurning(value) {
    var activeBtn = $('.activeBtn');
    var activeBox = $('.activeBox');
    var Box = [];
    var Btn = [];
    Btn[0] = $('#selfIntroductionBtn');
    Btn[1] = $('#myOrderBtn');
    Btn[2] = $('#myCreditBtn');
    Btn[3] = $('#shoppingHistoryBtn');
    Box[0] = $('#selfIntroductionBox');
    Box[1] = $('#myOrderBox');
    Box[2] = $('#myCreditBox');
    Box[3] = $('#shoppingHistoryBox');

    activeBtn.removeClass('active');
    activeBtn.removeClass('activeBtn');

    activeBox.fadeToggle('normal', function() {
        activeBox.removeClass('activeBox');
        Box[value-1].fadeToggle('normal', function() {
            Box[value-1].addClass('activeBox');
        });
    });
    Btn[value-1].addClass('active');
    Btn[value-1].addClass('activeBtn');
}
