// $(function(){
    // $("#btnRegister").click(function(e){
    //     e.preventDefault();
    //     // alert("fuck");
    //     $.ajax({
    //         url: '/reg',
    //         data: $('#formRegister').serialize(),
    //         type: 'POST',
    //         success: function(response) {
    //             console.log(response);
    //         },
    //         error: function(error) {
    //             console.log(error);
    //         }
    //     });
    // });
// });

// Switch channel + do commands dialog and confirm
$('#modal1').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var recipient = button.data('w2') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this)
    // modal.find('.modal-title').text('New message to ' + recipient)
    // modal.find('.modal-body input').val(recipient)
    modal.find('#modal1target').text(recipient)
})

$('#btnyes').click(function(){
    var _cmd = document.getElementById('modal1target').innerHTML;
    setTimeout(()=>{
        $('#modal1').modal('toggle');
        console.log("Hello!"+_cmd); 
        $('.overlay').addClass("show");
        $('.spanner').addClass("show");
        setTimeout(() => { 
            // console.log("World!"); 
            // $('.overlay').removeClass("show");
            // $('.spanner').removeClass("show");
            $.ajax({
                method: "POST",
                url: "/api/v1_0/swich",
                data: { name: "John", location: "Boston", cmd: _cmd }
            }).done(function(resp) {
                $('.overlay').removeClass("show");
                $('.spanner').removeClass("show");
                $modal = $('<div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="exampleModalLabel">Result</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><p>'+resp.htmlmsg+'</p></div><div class="modal-footer"><button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button></div></div></div></div>');
                $('body').append($modal);
                setTimeout(()=>{
                    $modal.modal('show');
                }, 100);
                console.log(resp);
            }).fail(function() {
                alert( "error" );
            });
        }, 100);
    }, 100);
});

// edit fullname profile box
$(document).ready(function(){
    $("#profilefullnamelink").click(function(){
        $("#profilefullnameedit").removeAttr('readonly');
        $("#profilefullnameedit").removeAttr('style');
        $("#profilefullnameedit").attr('style', 'border: 1px dashed green;');
    });
    // Update the input when lost focus
    $("#profilefullnameedit").focusout(function(){
        $("#profilefullnameedit").prop('readonly', true);
        $("#profilefullnameedit").prop('style', 'border: none;');
    });
    //
    $("#updateUserInfoBtn").click(function(){
        var _id = document.getElementById('profileuserid').innerHTML;
        var _email = document.getElementById('profileuseremail').innerHTML;
        var _fullname = document.getElementById('profilefullnameedit').value;
        setTimeout(()=>{
            $('.overlay').addClass("show");
            $('.spanner').addClass("show");
            setTimeout(()=>{
                $.ajax({
                    method: "POST",
                    url: "/api/v1_0/updateuser",
                    data: { id: _id, email: _email, fullname: _fullname }
                }).done(function(resp) {
                    // console.log(resp);
                    $('.overlay').removeClass("show");
                    $('.spanner').removeClass("show");
                    $modal = $('<div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="exampleModalLabel">Result</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><p>'+resp.htmlmsg+'</p></div><div class="modal-footer"><button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button></div></div></div></div>');
                    $('body').append($modal);
                    $modal.modal('show');
                }).fail(function() {
                    alert( "error" );
                });
            },10);
        },10);
    });
});

// update the fullname
