//PREVENT DEFAULT!!!!!!
$('#btnSend').click(function(){
  console.log("This was clicked!");
var form = $('form').serializeArray()
var $response = $('#response')
$.ajax({
    type: 'GET',
    url: '/submit',
    data: JSON.stringify(form),
    dataType: 'JSON',
    contentType: 'application/json',
    processData: true,
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
