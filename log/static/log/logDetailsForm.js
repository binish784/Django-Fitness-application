$(document).ready(function(){

	getAvailableSets();
	getLogTable();


$("#setSelection").change(function(){
	setValue=$("#setSelection").val();
	$exeEndpoint="/fitness/api/"+setValue+"/workout-list";
	$.ajax({
		method:"GET",
		url:$exeEndpoint,
		success:function(data){
			$("#exerciseSelection").html("");
			$.each(data,function(index,item){
				$("#exerciseSelection").append("<option value="+item.id+" > "+item.name+"</option>");
			})
		},
		error:function(error_data){
			console.log(error_data);
		}
	});
})


$("#logCreation").on("click",function(e){
		
		$exercise=$("#exerciseSelection").val();
		$log=$("#logDesc").val();
		$num_of_set=$("#num_of_set").val();
		$num_of_reps=$("#num_of_reps").val();
		$weights_used=$("#weights_used").val();
 
	$.ajax({
		method:"POST",
		url:'/logs/api/'+$log+'/log-details-write/',
		contentType:'application/json',
		datatype:'json',
		data:JSON.stringify({
			"parent_log": $log,
        	"exercise": $exercise,
        	"num_of_sets": $num_of_set,
        	"reps": $num_of_reps,
        	"weight_used":$weights_used
		}),
		success:function(data){
			console.log("Form Submission Successful");
			updateLog($log);
		},
		error:function(error_data){
			console.log("Error in form submission");
		}
	})
})




})


function updateLog($log){
	$logs={}
	$.ajax({
		method:'GET',
		url:'/logs/api/'+$log+'/log-details-read/',
		success:function(data){
			$(".logDetails").html("");
			logs=data;
			$.each(logs,function(index,item){
				$(".logDetails").append("<span>"+item.exercise+"&nbsp;&nbsp;&nbsp;"+item.num_of_sets+"&nbsp;&nbsp;&nbsp;"+item.reps+"&nbsp;&nbsp;&nbsp;"+item.weight_used+"</span><br>");
			})
			$("#num_of_reps").val(0);
			$("#weights_used").val(0);
		},
		error:function(error_data){
			console.log("Error in form submission");
		}
	})
}

function getAvailableSets(){
		$setEndpoint="/fitness/api/workout-set/"
		var $exeEndpoint;
		$.ajax({
		method:"GET",
		url:$setEndpoint,
		success:function(data){
			$.each(data,function(index,item){
				if(index==0){
					$("#setSelection").append("<option value="+ item.id +" selected> "+ item.name+"</option>");
					$exeEndpoint="/fitness/api/"+item.id+"/workout-list";
					ajaxCall2($exeEndpoint);				
				}
				else{
					$("#setSelection").append("<option value="+ item.id +"> "+ item.name+"</option>");
				}
			})
		},
		error:function(error_data){
			console.log(error_data);
		}
	})
	
}

function getLogTable(){
	$log=$("#logDesc").val()
	$.ajax({
			method:'GET',
			url:'/logs/api/'+$log+'/log-details-read/',
			success:function(data){
				$(".logList").append(
				'<li class="list-group-item">'+
						'<div class="row ">'+
								'<div class="col-sm-6">'+
									'<b>'+
										'Workout'+
									'</b>'+
								'</div>'+
								'<div class="col-sm-2">'+
									'<b>'+
										'Sets'+
									'</b>'+
								'</div>'+
								'<div class="col-sm-2">'+
									'<b>'+
										'Reps'+
									'</b>'+
								'</div>'+
								'<div class="col-sm-2">'+
									'<b>'+
										'weights'+
									'</b>'+
								'</div>'+
							'</div>'+
					'</li>'	
				);
				$.each(data,function(index,item){
				$updateLink="/logs/"+item.id+"/updateRecord";
				$deleteLink="/logs/"+item.id+"/confirm_delete";
				$(".logList").append(
					'<li class="list-group-item padding-0 logRow">'+
						'<div class="container-fluid">'+
							'<div class="row">'+
								'<div class="col-sm-6">'+
									'<div class="container-fluid">'+
										'<div class="row">'+
											'<div class="col-sm-8">'+
												item.exercise+
											'</div>'+
											'<div class="col-sm-4">'+
												'<div class="updateField">'+
													'&nbsp;&nbsp;<a href="'+$deleteLink+'" id='+item.id+'>Delete</a>'+
												'</div>'+
											'</div>'+
										'</div>'+
									'</div>'+
								'</div>'+
								'<div class="col-sm-2">'+
									item.num_of_sets+
								'</div>'+
								'<div class="col-sm-2">'+
									item.reps+
								'</div>'+
								'<div class="col-sm-2">'+
									item.weight_used+
								'</div>'+
							'</div>'+
						'</div>'+
					'</li>');
				})
			}
		})
}
	
	


function ajaxCall2($exeEndpoint){
	$.ajax({
		method:"GET",
		url:$exeEndpoint,
		success:function(data){
			$("#exerciseSelection").html("");
			$.each(data,function(index,item){
				$("#exerciseSelection").append("<option value="+item.id+" > "+item.name+"</option>");
			})
		},
		error:function(error_data){
			console.log(error_data);
		}
	})
}
