

var root = 'http://localhost:5000';
	function getAllCampaign() {
		$.ajax({
  			url: root + '/campaign',
  			method: 'GET',
  			dataType: "json",
  			success: function(data) {
  				console.log(data);
  			}
		});
	};

	function addCampaign() {
		$.ajax({
			url: root + '/posts',
  			method: 'POST',
  			data: {
			    title: 'foo',
			    body: 'bar',
			    userId: 1
			},
			success: function(data) {
  				console.log(data);
			}
		});
	}

	function getResponse(id) {
		$.ajax({
  			url: root + '/campaign/' + id + '/comment',
  			method: 'GET',
  			dataType: "json",
  			success: function(data) {
  				console.log(data);
  			}
		});
	}

	function addResponse(id) {
		$.ajax({
			url: root + '/campaign/' + id + '/comment',
  			method: 'POST',
  			data: {
			    title: 'foo',
			    body: 'bar',
			    userId: 1
			},
			success: function(data) {
  				console.log(data);
			}
		});
	}

	function calcResponse() {

	}

	function calcMostSuggestedLocation() {

	}

	function calcOfficeClosest() {

	}