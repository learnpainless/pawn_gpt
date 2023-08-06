jQuery(document).ready(function () {

    $(".chat-list a").click(function () {
        $(".chatbox").addClass('showbox');
        return false;
    });

    $(".chat-icon").click(function () {
        $(".chatbox").removeClass('showbox');
    });

    $('#send_btn').click(function () {
        let msg = $('#message_box').val()
        $('#message_box').val('')

        let li = `<li class="repaly">
                    <p>${msg}</p>
                  </li>`
        $('.msg-body ul').append(li)

        $.ajax({
            url: '/send_message',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                msg: msg
            }),
            success: function (res) {
                // console.log(res)
                let aiMsg = res['message']
                let li = `<li class="sender">
                    <p>${aiMsg}</p>
                  </li>`
                $('.msg-body ul').append(li)
            }
        })
    })

});