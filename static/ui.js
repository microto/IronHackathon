$(document).ready(function(){
	$(".movetowhitelist").click(function(){
		console.log($(this).attr('ip'));
		data = $(this).attr('ip');
		$.post("/",data, function(){alert('succes');return false;}).fail(function(){alert('fail');return false;})
		return false;
	})
})
