$(document).ready(function() {

	$( ".show" ).click(function() {
		$( "#user-pic" ).animate({ "left": "-=280px" }, "slow" );
	});
	 
	$( ".hide" ).click(function(){
		$( "#user-pic" ).animate({ "left": "+=280px" }, "slow" );
	});
	
	$("#shbutton1").click(function(){
		$(this).toggle();
	});
	
	$( ".showhide" ).click(function(){
		$("#user-info").slideToggle();
	});	
	
	$("#shbutton2").click(function(){
		$("#shbutton1").toggle();
	});
	
});