var ctx_one_hand = document.getElementById("one_hand_chart").getContext("2d");
var ctx_second_hand = document.getElementById("second_hand_chart").getContext("2d");

var one_hand_chart_data = {
	labels : one_hand_time_array,
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : one_hand_price_array
		}
	]
}

var second_hand_chart_data = {
	labels : second_hand_time_array,
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : second_hand_price_array
		}
	]
}

var oneHandChart = new Chart(ctx_one_hand).Line(one_hand_chart_data,{
            responsive: true,
            scaleShowGridLines : true,
        });

var secondHandChart = new Chart(ctx_second_hand).Line(second_hand_chart_data,{
            responsive: true,
            scaleShowGridLines : true,
        });