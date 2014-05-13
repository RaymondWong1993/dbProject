$(document).ready(function() {
	var informationBtn = $("#informationBtn");
    var orderBtn = $("#orderBtn");
    var menuBtn = $('#menuBtn');
    var deleteBtns = $('.glyphicon');
    var addBtn = $('#addBtn');
    var sure_addBtn = $('#sure_addBtn');
    var cancel_addBtn = $('#cancel_addBtn');
    changeBtn();
    informationBtn.click(function() {
        pageTurning(1);
    });
    orderBtn.click(function() {
        pageTurning(2);
    });
    menuBtn.click(function() {
        pageTurning(3);
    });
    $('body').on('click', '.glyphicon', function() {
        var id = $(this).attr('id');
        id = id.substr(9);
        id = parseInt(id);
        deleteBox(id);
    }); 
    addBtn.click(function() {
        showAddBox();
    });
    sure_addBtn.click(function() {
        addFood();
        postData();
    });
    cancel_addBtn.click(function() {
				cancel();
		});
});

function cancel() {
		$('#addBox').slideToggle('slow');
		$('#sure_addBtn').fadeToggle('normal');
		$('#cancel_addBtn').fadeToggle('normal', function() {
				$('#addBtn').fadeToggle('normal');
		});

    $('#addFoodImage').val('');
		$('#addFoodName').val('');
		$('#addFoodKinds').val('');
		$('#addFoodPrice').val('');
		$('#addFoodIntro').val('');
}

function postData() {
		var image = $('#addFoodImage').val();
		var name = $('#addFoodName').val();
		var price = $('#addFoodPrice').val();
		var kinds = $('#addFoodKinds').val();
		var describe = $('#addFoodIntro').val();
		$.post('/myRestaurant/',
					 {
							 image: image,
							 name: name,
							 price: price,
							 kinds: kinds,
							 describe: describe
					 });
}

function changeBtn() {
    $('#signInBoxBtn').css('display','none');
    $('#registerBtn').css('display', 'none');
    $('#logoutBtn').css('display', 'block');
    $('#myRestaurantBtn').css('display', 'block');
}

function pageTurning(value) {
    var activeBtn = $('.activeBtn');
    var activeBox = $('.activeBox');
    var Box = [];
    var Btn = [];
    Btn[0] = $('#informationBtn');
    Btn[1] = $('#orderBtn');
    Btn[2] = $('#menuBtn');
    Box[0] = $('#informationBox');
    Box[1] = $('#orderBox');
    Box[2] = $('#menuBox');

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

function deleteBox(id) {
    var foodBox = '#foodBox' + id;
    $(foodBox).slideToggle("slow", function() {
        $(foodBox).remove();
    });
}

function showAddBox() {
    var addBox = $('#addBox');
    var sure_addBtn = $('#sure_addBtn');
    var addBtn = $('#addBtn');
    var cancel_addBtn = $('#cancel_addBtn');
    addBtn.fadeToggle('slow', function() {
				sure_addBtn.fadeToggle('slow');
				cancel_addBtn.fadeToggle('slow');
		});
    addBox.slideToggle("slow", function() {
        var offset = parseInt($('body').scrollTop()) + 200;
        $('body').scrollTop(offset);
    });
}

function getPath(fileQuery, id) {
		var file = fileQuery[0].files[0];
		var reader = new FileReader();
    reader.onload = function(e) {
				$('#foodBox'+id).find('img').attr('src', e.target.result);
		};
    reader.readAsDataURL(file);
}

function addFood() {
    var image = $('#addFoodImage');
    var foodName = $('#addFoodName').val();
    var foodPrice = $('#addFoodPrice').val();
    var foodIntro = $('#addFoodIntro').val();
    var foodKinds = $('#addFoodKinds').val();
    // image = image.split("\\");
    // image = "/static/images/" + image[image.length-1];
    // hide add box
    var addBox = $('#addBox');
    var sure_addBtn = $('#sure_addBtn');
    var addBtn = $('#addBtn');
    var foodBoxs = $('.foodBoxs');
    var id = $(foodBoxs[foodBoxs.length - 1]).attr('id').substr(7);
    id = parseInt(id) + 1;

    addBox.slideToggle("slow");
    sure_addBtn.fadeToggle("slow",function() {
        // add new foodBox
        var newNode  = '<a href="javascript:void(0)" class="list-group-item foodBoxs" style="overflow: hidden;" id="foodBox'+id+'">'+
        '<div class="row myOrderRow">'+
        '<img class="col-xs-3" src="'+'" style="width: 200px; height: 150px;"/>'+
        '<div class="col-xs-2">'+
        '  <p>菜名：</p>'+
        '  <p>'+foodName+'</p>'+
        '</div>'+
        '<div class="col-xs-2">'+
        ' <p>单价：</p>'+
        ' <p>'+foodPrice+'元/份</p>'+
        '</div>'+
				'<div class="col-xs-2">'+
				' <p>菜系：</p>'+
				' <p>'+foodKinds+'</p>'+
				'</div>'+
        '<div class="col-xs-3">'+
        ' <p>介绍：</p>'+
        ' <p>'+foodIntro+'</p>'+
        '</div>'+
        '<div>'+
        ' <span class="glyphicon glyphicon-remove" style="float: right; margin-right: 10px;" id="deleteBtn'+id+'"></span>'+
        '</div>'+
        '</div>'+
        '</a>'
        $('#mainFoodBox').append(newNode);
        getPath(image, id);
        addBtn.fadeToggle("slow");
        $('#addFoodName').val('');
        $('#addFoodImage').val('');
        $('#addFoodIntro').val('');
        $('#addFoodPrice').val('');
				$('#addFoodKinds').val('');
        var offset = parseInt($('body').scrollTop()) + 400;
        $('body').scrollTop(offset);
    });
}
