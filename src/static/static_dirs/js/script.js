$(document).ready(function() {
    $(".button-collapse").sideNav();
    // $('body').hide()
    // site preloader -- also uncomment the div in the header and the css style for #preloader
    // $(window).load(function() {
    //     $('.progress').fadeOut('slow');
    //     // $('body').show();
    // });
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        //>=, not <=
        if (scroll >= 100) {
            //clearHeader, not clearheader - caps H
            $(".main_page").addClass("animated fadeInUp");
        }
    }); //missing );

});
