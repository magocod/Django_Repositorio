//response
$(".button-collapse").sideNav();
 
//carusell
$(document).ready(function(){
      $('.carousel').carousel();
    });

$('.carousel.carousel-slider').carousel({fullWidth: true});
 
//discovery
$('.tap-target').tapTarget('open');
$('.tap-target').tapTarget('close');


//modal
$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
    //campos seleccion
    $('select').material_select();
    



});



 