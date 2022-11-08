$(document).ready(function(){
  $("input[type='text']").on("keypress",function(event){
    if(event.which===13){
      var data=$('form input').val();
      var todo=data
      // console.log(todo)
      $.ajax({
        type:'POST',
        url:'todos/',
        data:data,
        contentType: "application/json",
        dataType: "json",
        success: function(data){
          location.reload();
        },
      });
  }
  });
  $('li').on("click",function(){
    var item=$(this).text();
    item=item.trim()
    $.ajax({
      type:'DELETE',
      url:'/todos/',
      data:item,
      success:function(data){
        location.reload();
      }
    });
  });

$("ul").on("click", "li", function () {
	$(this).toggleClass("complete")
});

$(".fa-plus").click(function () {
	$("input[type='text']").fadeToggle()
});
});
