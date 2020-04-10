
var user_id = Math.random().toString().slice(2,8);

var trial_string = `https://inversepictionary.github.io/writer.html?trial_id=0&user_id=${user_id}`;
var practice_string = `https://inversepictionary.github.io/writer.html?trial_id=0&user_id=${user_id}`;

$(document).ready(function(){
    $("#start").attr('href', trial_string);
    $("#agree").click(function(){
    	$("#page1").css("display", "none");
    	$("#task_description").css("display", "unset");
    });
    $("#check_answer").click(function () {
    	let ans1 = $("input[name='gridsize']:checked").val();
    	let ans2 = $("input[name='nnocolor']:checked").val();
    	let ans3 = $("input[name='exptask']:checked").val();
    	if (ans1 == "15" && ans2 == "1" && ans3 == "fewest") {
    		window.location = `${practice_string}`
    	} else {
    		alert("some quiz answer(s) are wrong, please correct them first before continuing")
    	}
    });
});
