$(function(){
				setInterval(oneSecondFunction, 1000);
			});

			function oneSecondFunction() {
				// update table every second
				$.ajax({
				        url: '/list_calculations',
				        data: {
				  
				        },
				        dataType: 'json',
				        success: function (data) {
				          console.log(data["data"][0])
				        }
				      });
			}