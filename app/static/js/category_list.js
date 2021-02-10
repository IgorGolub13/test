var user_input = $("#unique-input")
var search_icon = $('#search-icon')
var artists_div = $('#replaceable-content')
var endpoint_category = '/app/category'
var endpoint_transaction = '/app/transaction'
var delay_by_in_ms = 700
var scheduled_function = false

var ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the artists_div, then:
            artists_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                artists_div.html(response['html_from_view'])
                // fade-in the div with new contents
                artists_div.fadeTo('slow', 1)
                // stop animating search icon
                search_icon.removeClass('blink')
            })
        })
}
// $(document).ready(function () {
//     {
//         q: $(this).val() // value of user_input: the HTML element with ID user-input
//     }
// });

user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }

    // start animating the search icon with the CSS class
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint_category, request_parameters)
})


$( "#selected-category" ).change(function() {
    const request_parameters = {
        q: $(this).val() // value of user_input: the HTML element with ID user-input
    }
    console.log(request_parameters)

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }
    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint_transaction, request_parameters)
});

$("#category-clear-button").click(function(){
    $("#transaction-describe :input").val('');
 });

$("#transaction-clear-button").click(function(){
    $("#category-name :input").val('');
    $("#category-description :input").val('');
 });