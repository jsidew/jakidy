$(function() {

var jQT = $.jQTouch({
    icon: 'icon.png',
    statusBar: 'black'
});


$("#newfood .cancel").on('click', function() {
    $('#newfood form').trigger('reset');
});

$('#newfood form').on('submit', function() {
    $.post('/food/save', $(this).serialize(), function(data) {
        if(data.message !== 'OK') {
            console.error(data.message);
        } else {
            $("#newfood .cancel").trigger('click');
        }
    }, 'json').fail(function() {
        console.error('something went wrong!');
    });
    return false;
});


});
