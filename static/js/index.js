$('#start').click(function () {
    $('#start').css("disabled", "disabled")
    d = {
        "links": $('#links').val(),
        "scripts": $('#scripts').val(),
        "start_sleep": $('#start_sleep').val(),
        "sleep_second": $('#sleep_second').val()
    }
    $.get('/run', d, function (data) {
        $('#result').val(data)
    })
    $('#start').css("disabled", "")
})