var user_input_tr = $("#selected-category")
var search_icon_tr = $('#srch-icon')
var artists_div_tr = $('#rpble-content')
var endpoint_tr = '/app/transaction'
var delay_by_in_ms_tr = 700
var scheduled_function_tr = false

var ajax_call = function (endpoint_tr, request_parameters_tr) {
    $.getJSON(endpoint_tr, request_parameters_tr)
        .done(response => {
            // fade out the artists_div, then:
            artists_div_tr.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                artists_div_tr.html(response['html_from_view'])
                // fade-in the div with new contents
                artists_div_tr.fadeTo('slow', 1)
                // stop animating search icon
                search_icon_tr.removeClass('blink')
            })
        })
}
$(document).ready(function () {
    {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }
});

user_input_tr.on('selected', function () {

    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }

    // start animating the search icon with the CSS class
    search_icon_tr.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function_tr) {
        clearTimeout(scheduled_function_tr)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function_tr = setTimeout(ajax_call, delay_by_in_ms_tr, endpoint_tr, request_parameters_tr)
})