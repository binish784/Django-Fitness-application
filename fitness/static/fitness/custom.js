
	$(document).ready(function(){
	
		var barEndPoint='/fitness/api/list-weight';
		var lineEndPoint='/fitness/api/monthly-weight';

		data=[]
		labels=[]
		maximum_gain=0

		//Ajax for bar graph

		$.ajax({
			method:"GET",
			url:barEndPoint,
			success:function(data){
				var ctx = document.getElementById("myChart").getContext('2d');
				var myChart = new Chart(ctx, {
				    type: 'bar',
				    data: {
				        labels: data.labels,
				        datasets: [{
				            label: 'Weights this week',
				            data: data.weights,
				        }]
				    },
					options: {
	       				scales: {
	            			yAxes: [{
	                			ticks: {
	                				// minimum of data.weights - 10 or 20 = min
	                    			min:Math.min.apply(Math,data.weights)-20,
	                			}
	            			}]
	        			}
	    			}
	    		});
				maximum_gain=data.max_weight
				$("#maxGain").html(maximum_gain)
			},
			error:function(error_data){
				console.log(error_data);
			}
		})
	
		//Ajax call for line graph
		data=[]
		labels=[]
		$.ajax({
			method:"GET",
			url:lineEndPoint,
			success:function(data){
				
				var ctx = document.getElementById("monthlyChart").getContext('2d');
				var myChart = new Chart(ctx, {
				    type: 'line',
				    data: {
				        labels: data.labels,
				        datasets: [{
				            label: 'Monthly Weight Statistic',
				            data: data.weights,
				        }]
				    }, 
				});
				maximum_gain=data.max_weight
				$("#maxGain").html(maximum_gain)
			},
			error:function(error_data){
				console.log(error_data);
			}
		})


	})