$('#add_item').on('click', function() {
    $('ul.my_list').append('<li>Item</li>');
});
$('#remove_item').on('click', function () {
    $('li:last').remove();
});
$('#clear_list').on('click', function () {
    $('li').remove();
});
