jQuery(document).ready(function($) {
	vote_value = $('#vote_value').html();
	if(vote_value == 1){
		$('#id_value_0').attr('checked',true);
	}else if(vote_value == -1){
		$('#id_value_1').attr('checked',true);
	}else{
		console.log('nothing');
	}
});
