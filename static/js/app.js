let currAddr = ''
let currPasswd = ''

$(document).ready(function() {
    if (document.location.pathname === '/storage/') {
        currAddr = $('#addr').text()
        currPasswd = $('#passwd').text()
        miniChart('myfirstchart')
        miniChart('myfirstchart2')
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

function miniChart(el) {
    new Morris.Line({
      // ID of the element in which to draw the chart.
      element: el,
      element1: el,
      // Chart data records -- each entry in this array corresponds to a point on
      // the chart.
      data: [
        { year: '2008', value: 20, value1: 30 },
        { year: '2009', value: 10, value1: 20 },
        { year: '2010', value: 5, value1: 25 },
        { year: '2011', value: 5, value1: 15 },
        { year: '2012', value: 20, value1: 35 }
      ],
      // The name of the data record attribute that contains x-values.
      xkey: 'year',
      // A list of names of data record attributes that contain y-values.
      ykeys: ['value', 'value1'],
      // Labels for the ykeys -- will be displayed when you hover over the
      // chart.
      labels: ['Value']
    });
}