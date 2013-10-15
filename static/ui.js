$(document).ready(function(){
	$(".movetowhitelist").click(function(){
		console.log($(this).attr('ip'));
		data = $(this).attr('ip');
		$.ajax({
		  type: "POST",
		  url: '/whitelist',
		  data: data,
		  success: function() {
		  	alert('done');
		  },
		  fail: fuction() {
		  	alert('done');
		  	return false;
		  }
		  dataType: dataType
		});
		return false;
	})
})