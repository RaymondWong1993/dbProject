#(document).ready(function() {
    var deleteBtns = $('#mainFoodBox').find('span');
    var addBtn = $('#addBtn');
    deleteBtns.each(function() {
				$(this).click(function() {
						deleteFood(this);
				});
		});
    addBtn.click(function() {
				addFood();
		});
})

deleteFood(btn) {
    var id_ = $(btn).attr(id);
		id_ = parseInt(id_);
    var foodName = '#name' + toString(id_);
    foodName = $(foodName).text();
		$.post('/order/remove/',
					 {
							 'name': foodName
					 },
					 function(data, status) {
							 if (data.resp == 1) {
									 alert('删除成功！');
							 } else {
									 alert('删除失败！');
							 }
					 });
		
}
