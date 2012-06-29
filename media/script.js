var update_digest = false;
var default_errors_count = 0;
var title_interval_id = 0;
var document_original_title = '';

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

$(document).ready(function () {
	$("#min_select :first").attr("selected", "selected");
	$("#edit_patterns_button").button();
	$("#show_all_patterns_button").button();
	document_original_title = document.title;
	setInterval(function () {
		if (update_digest == true) {
			$("#content").load('digest/', check_default_errors_count);
		}
	}, 60000);
});

show_all_patterns = function(){
	$(".zero_pattern").css("display", "table-row");
};

check_default_errors_count = function () {
	var count = parseInt($("#default_pattern").next().next().text());
	if (count > 10 && (default_errors_count == 0 || count / default_errors_count > 2)) {
		title_interval_id = setInterval(title_blink, 1000);
		$(window).focus(function () {
			if (title_interval_id != 0) {
				clearInterval(title_interval_id);
				title_interval_id = 0;
				document.title = document_original_title;
			}
		});
	}
	default_errors_count = count;
};

title_blink = function () {
	if (document.title != 'Too many errors...') {
		document.title = 'Too many errors...';
	} else {
		document.title = document_original_title;
	}
};

edit_patterns = function(){
	update_digest = false;
	$("#all_patterns").load("patterns/all/",
		function(data){
			$("#all_patterns").dialog({
				title: 'Все шаблоны',
				modal: true,
				width: 560,
				close: function(event, ui){
					$(this).empty();
					update_digest = true;
				}
			})	;
			$("#all_patterns").dialog('option', 'buttons', [
				{text: 'Сохранить',
				click: function(){
					$.post("patterns/save/", {data: $("#all_patterns_textarea").val()})
					$("#all_patterns").dialog('close');
					$("#content").load('/digest/');			
				}}				
			]);
		}
	);
}

open_pattern = function(hash, minutes){
	window.location = "pattern?hash=" + hash + "&min=" + minutes;
};

