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

