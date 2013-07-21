$(function() {


window.jQT = $.jQTouch({
    icon: 'icon.png',
    statusBar: 'black',
    useFastTouch: false
});

var nextLink = function(e) {
    e.preventDefault();
    $.get(
        e.data.uri,
        function(data) {
            $(e.data.selector).remove();
            $('body').append(data);

            if(e.data.cb) {
                e.data.cb();
            }

            jQT.goTo(e.data.selector, 'slideright');
        },
        'html'
    );
    return false;
};

$('#home a[href="#foodlist"]').on(
    'click',
    {
        uri: '/food/list',
        selector: '#foodlist',
        cb: function() {
            $('#foodlist .content a').on('click', function() {
                
                var nfInputs = $('#newfood input'), p = $(this).parent();
                
                nfInputs.filter('[name="id"]').val(p.data('id'));
                nfInputs.filter('[name="name"]').val(p.data('name'));
                nfInputs.filter('[name="protein"]').val(p.data('protein'));
                nfInputs.filter('[name="carbs"]').val(p.data('carbs'));
                nfInputs.filter('[name="fat"]').val(p.data('fat'));
                nfInputs.filter('[name="price"]').val(p.data('price'));
                
                $(this).attr('href', '#newfood');
                
            });
        }
    },
    nextLink
);
$('#home a[href="#meals"]').on(
    'click',
    { uri: '/food/meals', selector: '#meals',
        cb: function() {
            $('#meals p.label').each(function(){
                $(this).html($(this).text().replace(/\n/g, '<br/>'));
            });
            $('#newmeal input[type="checkbox"]')
                .prop('disabled', true)
                .on('change', function() {
                    if(!$(this).prop('checked')) {
                        $(this).siblings('input[type="number"]').val(null);
                        $(this).prop('disabled', true);
                    }
                }
            );
            $('#newmeal input[type="number"]').on('change', function() {
                if($(this).val() > 0) {
                    $(this).siblings('input[type="checkbox"]')
                        .prop('disabled', false)
                        .prop('checked', true);
                } else {
                    $(this).siblings('input[type="checkbox"]')
                        .prop('disabled', true)
                        .prop('checked', false);
                }
            });
            $('#newmeal form').on('submit', function() {
                $(this).find('input[name^="food"]:checked').each(function() {
                    $(this).val($(this).siblings('input[name^="grams"]').val());
                });
                $.post(
                    '/food/savemeal',
                    $(this).serialize().replace(/&grams.+?=[^&]*/g, ''),
                    function(data) {
                        console.log(data);
                        if(data.message !== 'OK') {
                            console.error(data.message);
                        } else {
                            $("#newmeal").remove();
                            jQT.goTo('#home');
                        }
                    },
                    'json'
                ).fail(function() {
                    console.error('something went wrong!');
                });
                return false;
            });
        }
    },
    nextLink
);


$("#newfood .cancel").on('click', function(e) {
    $('#newfood form').trigger('reset');
});

$('#newfood form').on('submit', function() {
    $.post('/food/save', $(this).serialize(), function(data) {
        if(data.message !== 'OK') {
            console.error(data.message);
        } else {
            $('#newfood form').trigger('reset');
            jQT.goTo('#home');
        }
    }, 'json').fail(function() {
        console.error('something went wrong!');
    });
    return false;
});


});
