$('#btnSend').click(function(event){
  event.preventDefault()
  console.log("This was clicked!");
  var user_submission = $('form').serializeArray()
  $.ajax({
      type: 'POST',
      url: '/response',
      data: JSON.stringify(user_submission),
      dataType: 'JSON',
      contentType: 'application/json',
      processData: true,
      success: function (response) {
        console.log(response)
        $('#form').val(response)


  }
   });

});


function myFunction(){
    event.preventDefault()
    var x = document.getElementById("form");
    if (x.style.display === "none") {
        x.style.display = "inline";
    } else {
        x.style.display = "none";
    }
};

function selectResult(){
    function myFunctionYes(){
        event.preventDefault()
        var x = document.getElementById("results_yes");
        if (x.style.display === "none") {
            x.style.display = "inline";
        } else {
            x.style.display = "none";
        }
    };

    function myFunctionNo(){
        event.preventDefault()
        console.log(prediction);
        var x = document.getElementById("results_no");
        if (x.style.display === "none") {
            x.style.display = "inline";
        } else {
            x.style.display = "none";
        }
    };

    if (response == {"prediction":[0]}){
        myFunctionYes();
    } else {
        myFunctionNo();
    }
};
