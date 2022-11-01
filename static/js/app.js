let contr = ''
let currAddr = ''
let currPasswd = ''

$(document).ready(function() {
    if (document.location.pathname === '/storage/') {
        contr = $('#contr').text()
        currAddr = $('#addr').text()
        currPasswd = $('#passwd').text()
       getPoints()
        let intertval1 = setInterval(getCurrent, 2000)
    }
})

function getCurrent() {
    $.ajax({
        url: '/refresh?addr=' + currAddr + '&passwd=' + currPasswd,
        success: function (data) {
            $('#table').html(data)
            for (let i = 1; i<=4; i++) {
                if ($('#rele' + i).text() === '1') {
                    $('#relBtn' + i).removeClass('btn-danger')
                    $('#relBtn' + i).addClass('btn-success')
                }
                else {
                    $('#relBtn' + i).removeClass('btn-success')
                    $('#relBtn' + i).addClass('btn-danger')
                }
            }
        }
    })
}


$('.btn_sel').on('click', function (event) {
    controller = event.target.id
    $.ajax({
        url: '/storage?contr=' + controller,
        success: function (data) {
            if (data.slice(0, 4) === 'Fail') {
                $('#mal1').text("Контроллер не доступен");
                $('#mTitle').text(data.slice(5));
                $('#modAlert').modal("show")
            }
            else {
                window.open('/storage?contr=' + controller, '_self')
            }
        }
    })
})

$('.btn-back').on('click', function (event) {
    window.open('/', '_self')
})

$('.btn-rele').on('click', function (event) {
    let btn = event.target.id

    $('.btn-rele').prop('disabled', true)
    setTimeout(function () {
        $('.btn-rele').prop('disabled', false)
    }, 2000)

    $.ajax({
        url: '/keypress?rele=' + btn + '&addr=' + currAddr + '&passwd=' + currPasswd,
        success: function (data) {
            if (data == '200') {
                if (btn === 'allOff') {
                    $('.btn-rele').removeClass('btn-success')
                    $('.btn-rele').addClass('btn-danger')
                }
                if ($('#' + btn).hasClass('btn-success') === true) {
                    $('#' + btn).removeClass('btn-success')
                    $('#' + btn).addClass('btn-danger')
                }
                else if($('#' + btn).hasClass('btn-danger') === true) {
                    $('#' + btn).removeClass('btn-danger')
                    $('#' + btn).addClass('btn-success')
                }
                $('#allOff').removeClass('btn-success')
                $('#allOff').removeClass('btn-success')
                $('#allOff').addClass('btn-outline-danger')
            }
        }
    })
})

function getPoints() {
    $.ajax({
        url: '/chart/?contr=' + contr,
        success: function (data) {
            console.log(data)
            miniChart('chartA' ,data['channelA']['points'], data['channelA']['labels'])
            miniChart('chartB' ,data['channelB']['points'], data['channelB']['labels'])
        }
    })
}

function miniChart(element, data, keys) {
    new Morris.Line({
        element: element,
        data: data,
        xkey: 'Date',
        ykeys: keys,
        labels: keys,
        hideHover: 'auto',
        lineColors:['#FF0000', '#FFA500', '#FFFF00', '#008000', '#0000FF', '#000080',
            '#808080', '#800000', '#00FFFF', '#2F4F4F']
    });
}