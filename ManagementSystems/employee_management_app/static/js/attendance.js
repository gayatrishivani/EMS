$(document).ready(function(){
    $('.aten-nav a').on('click', e => {
        e.preventDefault();
    
        let $tablink = $(e.target);
        let $div_container = $tablink.closest('.wrap');
    
        $div_container.find('li').removeClass('active');
        $div_container.find('.tab-content-at').removeClass('current');
    
        let targetSelector = $tablink.attr('href');
        $tablink.parent().addClass('active');
        $(targetSelector).addClass('current');
    });
    
    $('.aten-nav li:nth-child(1) a').trigger('click');
    
    $('#button').click(function(e) {
        console.log('this is being clicked')
        e.preventDefault();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type:"POST",
            url:"/mark_attendance",
            data:{
                'instance': '',
                'arrival': '',
                'csrfmiddlewaretoken' : csrftoken, },
            dataType:'json',
            success: function(response) {
                $("#button").prop("disabled", true);
                //data from django responce
                // print('response',response.instance)
                // var instance = JSON.parse(response["instance"]); 
                // var attenm = JSON.parse(response["arrival"]);
                // console.log(attenm);
                // console.log(instance);
                // $("#h-at").text(attenm)
    
            },
            error: function(response){
                alert("there is error")
            }
        });
    } )
    
})