$('#start').click(function () {
    $('#start').attr("disabled", "disabled")
    start()
    d = {
        "links": $('#links').val(),
        "scripts": $('#scripts').val(),
        "start_sleep": $('#start_sleep').val(),
        "sleep_second": $('#sleep_second').val()
    }
    $.get('/run', d, function (data) {
        $('#result').val(data)
        $('#start').removeAttr("disabled")
        stop()
    })
})

$(function () {
    stop()
})

var timer
var ro = 0

function start() {
    $('#loading').show()
    timer = setInterval(function () {
        ro += 5
        $('#loading i').css('transform', "rotate(" + ro + "deg)")
    }, 5)
}

function stop() {
    clearInterval(timer)
    $('#loading').hide()
}

$('#save').click(function () {
    createHtml()
});

function createHtml() {
    try {
        download(
            $("#result").val(),
            "result");
    } catch (e) {
        alert(e);
    }
}

function download(content, fileName) {
    var a = document.createElement("a");
    var file = new Blob([content]);
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
}