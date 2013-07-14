$(function() {


window.jQT = $.jQTouch({
    icon: 'icon.png',
    statusBar: 'black',
    useFastTouch: false
});


$('#home .content a').on('click', function() {
    
    var nfInputs = $('#newfood input');
    
    nfInputs.filter('[name="id"]').val($(this).data('id'));
    nfInputs.filter('[name="name"]').val($(this).data('name'));
    nfInputs.filter('[name="protein"]').val($(this).find('.protein').data('val'));
    nfInputs.filter('[name="carbs"]').val($(this).find('.carbs').data('val'));
    nfInputs.filter('[name="fat"]').val($(this).find('.fat').data('val'));
    
    $(this).attr('href', '#newfood');
    
});

$("#newfood .cancel").on('click', function(e) {
    $('#newfood form').trigger('reset');
});

$('#newfood form').on('submit', function() {
    $.post('/food/save', $(this).serialize(), function(data) {
        if(data.message !== 'OK') {
            console.error(data.message);
        } else {
            window.location.hash = "#home";
            window.location.reload();
        }
    }, 'json').fail(function() {
        console.error('something went wrong!');
    });
    return false;
});


});
