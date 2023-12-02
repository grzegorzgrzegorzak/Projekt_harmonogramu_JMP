

document.addEventListener('DOMContentLoaded', function() {
    var rows = document.getElementsByTagName('tr');
//    console.log(rows)
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];

        row.addEventListener('mouseover', function() {
            var button = this.querySelector('td a');
            console.log(button, i);
            button.classList.remove('hidden-button');
        });

        row.addEventListener('mouseout', function() {
            var button = this.querySelector('td a');
            button.classList.add('hidden-button');
        });
    }
});

//"Dodawanie border line w zależności od tego czy sklep jest w realizacji czy nie"
//$(document).ready(function () {
//    $.ajax({
//        url: '/get_model_data',
//        method: 'GET',
//        success: function(model_data) {
//            var warunek = model_data.is_in_realization
//            var rows = document.getElementsByTagName('tr')
//            for (var i = 0; i < rows.length; i++) {
//                var row = rows[i];
//                if (warunek) {
//                    $(row).addClass("in-realization");
//                } else {
//                    $(row).removeClass("in-realization")
//                }
//            }
//        }})
//    });




//        var warunek = "{{ model_data.is_in_realization }}";
//        var rows = document.getElementsByTagName('tr');
//        console.log(rows)
//        console.log(warunek)
//        for (var i = 0; i < rows.length; i++) {
//            var row = rows[i];
//            if (warunek) {
//                row.classList.add("in-realization");
//            } else {
//                row.classList.remove("in-realization")
//            }
//        }
//
//});
//


