//PREVENT DEFAULT!!!!!!
$('#btnSend').click(function(){
  console.log("This was clicked!");
var form = $('form').serializeArray()
var $response = $('#response')
$.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:5000/submit',
    dataType: 'JSON',
    contentType: 'application/json',
    data: JSON.stringify(form),
    processData: false,
    success: function (data) {
           var tmp = data;
           console.log(tmp);
           //return tmp;
    //success: function(response){
        //$.each(response, function(i, response){
          //$orders.append('<li>data</li>');

        //});
        //cosnole.log(repsonse);


  }
   });

});
//});
