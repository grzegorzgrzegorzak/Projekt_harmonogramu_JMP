console.log('hello world')
const helloWorldBox = document.getElementById('rowsd')
const storeBox = document.getElementById('rowsd')


$(function() {
    $.get('/region_color_row/', function(response) {
        var store = response.data;
        var $element = $('.color-row');
        store.forEach(el => {
            if (el.region === 'LUB')    {
                console.log(el);
                console.log(store);
                $element.css('background-color', 'green');

            } else {
                console.log(el.region)
                $element.css('background-color', 'red');
            }
        });
    });
});
