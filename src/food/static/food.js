$(function() {

var jQT = $.jQTouch({
    icon: 'icon.png',
    statusBar: 'black'
});


$("#newfood .cancel").on('click', function() {
    $('#newfood form').trigger('reset');
});

$('#newfood form').on('submit', function() {
    alert($(this).serialize());
    return false;
});


});
