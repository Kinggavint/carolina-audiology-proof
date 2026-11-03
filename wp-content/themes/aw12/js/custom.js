(function($){

  const randomID = ( length = 5 ) => {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }


  //
  // Animations
  //

  let animationClassArray = [
    '.fadeIn',
    '.fadeBackgroundIn',
    '.slideLeft',
    '.slideRight',
    '.slideUp',
    '.slideDown',
    '.zoomIn',
    '.border-card .card-header',
    '.circle-icon',
    '.wp-block-cover-image',
    '.wp-block-cover__inner-container',
    '.wp-block-cover',
    '.bg-angle-right',
    '.bg-angle-left'
  ]

  let animationClasses = animationClassArray.join(', ');

  let checkAnimations = function() {
    $(animationClasses).not('.show').each(function() {
      let aboveFold = $(this).offset().top <= $(window).scrollTop() + $(window).height();
      let isSlide = $(this).parents('.carousel-item').length > 0;
      if (aboveFold && !isSlide) $(this).addClass('show');
    });
  }

  let adjustParallax = function() {
    $('.bg-parallax').css({
      'background-position': `center -${$(window).scrollTop() / 4}px`
    })
  }

  $(document).ready(function() {
    checkAnimations();
    adjustParallax();
  })

  $(window).scroll(function() {
    checkAnimations();
    adjustParallax();
  })


  //
  // Collapse
  //

  $('.btn-more').each(function() {
    let id = 'collapse-' + randomID();
    $(this).attr({
      'data-toggle': 'collapse',
      'data-target': '#' + id,
      'aria-expanded': 'false',
      'aria-controls': id
    });
    let collapse = $(this).parents('.wp-block-group').first().find('.collapse').first();
    collapse.attr({
      id: id
    });
  })

})(jQuery);

jQuery(document).ready(function($){
  $(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if (scroll > 30) {
      $(".sticky-bottom").fadeIn();
    }

    else{
      $(".sticky-bottom").fadeOut();    
    }
  })
})
