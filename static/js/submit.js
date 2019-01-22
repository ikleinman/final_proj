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
          $('#form').val(response)
          console.log(user_submission)
  }
   });

});

// $('#btnSend').click(function(event){
//     event.preventDefault()
//     console.log("This was clicked!");
//     var x = document.getElementById("myDIV");
//     if (x.style.display === "none") {
//         x.style.display = "block";
//     } else {
//         x.style.display = "none";
//     }
// });

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
        var x = document.getElementById("results_no");
        if (x.style.display === "none") {
            x.style.display = "inline";
        } else {
            x.style.display = "none";
        }
    };
    // myFunctionNo();
    // myFunctionYes();
    if (prediction == '0'){
        myFunctionYes();
    } else {
        myFunctionNo();
    }
}

// function myFunctionYes(){
//     event.preventDefault()
//     var x = document.getElementById("results_yes");
//     if (x.style.display === "none") {
//         x.style.display = "inline";
//     } else {
//         x.style.display = "none";
//     }
// };

// function myFunctionNo(){
//     event.preventDefault()
//     var x = document.getElementById("results_no");
//     if (x.style.display === "none") {
//         x.style.display = "inline";
//     } else {
//         x.style.display = "none";
//     }
// };