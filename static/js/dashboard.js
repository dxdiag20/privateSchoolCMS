/*
    Notice JavaScript
*/
$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-dashboard").modal("show");
            },
            success: function (data) {
                $("#modal-dashboard .modal-content").html(data.html_form);
            }
        });
    };
  
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#notice-table tbody").html(data.noticeList);  
                    $("#modal-dashboard").modal("hide");  
                    Lobibox.notify('success', {
                        sound: false,
                        delay: 900,
                        msg: 'Successfully completed'
                    });                    
                }
                else {
                    $("#modal-dashboard .modal-content").html(data.html_form);
                    Lobibox.notify('warning', {
                        sound: false,
                        delay: 900,
                        msg: 'Errors are captured'
                    });                    
                }
            }
        });
        return false;
    };


  /* Binding */ 
  // Create notice
  $("#notice-div").on('click', ".js-register-notice", loadForm);
  $("#modal-notice").on("submit", ".js-notice-register-form", saveForm);
  // Delete notice
  $("#notice-div").on("click", ".js-delete-notice", loadForm);
  $("#modal-dashboard").on("submit", ".js-notice-notice-form", saveForm);
});