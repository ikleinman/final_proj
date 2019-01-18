PREVENT DEFAULT!!!!!!
$('form').serializeArray()

$.ajax({

    url : '/submit',
    type : 'GET',
    data : {
        'numberOfAnswers' : 10
    },
    dataType:'json',
    success : function(data) {
        alert('Data: '+data);
    },
    error : function(request,error)
    {
        console.log("Request: "+JSON.stringify(request));
    }
});
