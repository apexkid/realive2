

var root = 'http://localhost:5000';
	function getAllCampaign() {
		$.ajax({
  			url: root + '/campaign/',
  			method: 'GET',
  			dataType: "json",
  			success: function(data) {
  				console.log(data);
  			}
		});
	};

	function getOneCampaign(id) {
	    $.ajax({
  			url: root + '/campaign/' + id,
  			method: 'GET',
  			dataType: "json",
  			success: function(data) {
  				console.log(data);
  			}
		});
	};

	function addCampaign(ntitle, ncity, nofficeLocation, nlocalityPref, npoi, nlivingCost, npriorities, nmove_in_date, nend_date, ndescription) {
		$.ajax({
			url: root + '/campaign/',
  			method: 'POST',
  			data: {
			    title: ntitle,
			    city: ncity,
			    officeLocation: nofficeLocation,
			    localityPref: nlocalityPref,
			    poi: npoi,
			    livingCost: nlivingCost,
			    priorities: npriorities,
			    move_in_date: nmove_in_date,
			    end_date: nend_date,
			    description: ndescription
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

	function addResponse(ncampaign_id, ncomment, ncod1, ncod2) {
		$.ajax({
			url: root + '/campaign/' + id + '/comment',
  			method: 'POST',
  			data: {
			    campaign_id: ncampaign_id,
			    content: ncomment,
			    cod1: ncod1,
			    cod2: ncod2
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
