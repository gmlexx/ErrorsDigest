var update_digest = false;

$('html').ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$(document).ready(function() {
	$("#min_select :first").attr("selected", "selected");
	$("#new_pattern_button").button();
	$("#edit_patterns_button").button();
    setInterval(function() {
            if(update_digest == true){
                $("#content").load('/digest/');
            }
        }, 60000);
});

edit_patterns = function(){
    update_digest = false;
	$("#all_patterns").load("/pattern/all/",
		function(data){
			$("#all_patterns").dialog({
				title: 'All patterns',
				modal: true,
				width: 560,
				close: function(event, ui){
					$(this).empty();
                    update_digest = true;
				}
			})	;
			$("#all_patterns").dialog('option', 'buttons', [
				{text: 'Save',
				click: function(){
					$.post("/patterns/save/", {data: $("#all_patterns_textarea").val()})
					$("#all_patterns").dialog('close');
					$("#content").load('/digest/');			
				}}				
			]);
		}
	);
}

open_pattern = function(hash, minutes){
    window.location = "/pattern/" + hash + "/" + minutes + "/";
};

