//PREVENT DEFAULT!!!!!!
$('#btnSend').click(function(){
  console.log("This was clicked!");
var form = $('form').serializeArray()
var $response = $('#response')
$.ajax({
    type: 'GET',
    url: '/submit',
    dataType: 'JSON',
    contentType: 'application/json',
    data: JSON.stringify(form),
    processData: false,
    success: function(response){
        //$.each(response, function(i, response){
          //$orders.append('<li>data</li>');

        //});
        cosnole.log(repsonse);
    }
    //error: function( jqXhr, textStatus, errorThrown ){

        //return( errorThrown );

});
});
