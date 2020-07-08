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
    setTimeout(()=>{
        $('#modal1').modal('toggle');
        console.log("Hello!"); 
        $('.overlay').addClass("show");
        $('.spanner').addClass("show");
        setTimeout(() => { 
            console.log("World!"); 
            $('.overlay').removeClass("show");
            $('.spanner').removeClass("show");
        }, 2000);
    }, 300);
});