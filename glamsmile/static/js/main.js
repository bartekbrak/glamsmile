// code by Janek@Hint, modified by tu-br

var currentSlide = document.URL.split("#")[1] || 1;

$.easing.jease = function (x, t, b, c, d) {
    return c * ( -Math.pow( 2, -10 * t/d ) + 1 ) + b;
}

function goTo(pageId) {
  var offset = $('#slide-'+pageId).data('offset');
  $('a.slideme').removeClass('current');
  $('a').css({borderTopWidth:0,opacity:1});

  var innerOffset=$('#slide-'+pageId).width();
  if(pageId<currentSlide) {
    innerOffset=-innerOffset;
  }
  $('#slide-'+pageId+' .content').css({left:innerOffset+'px'});
  $('#slide-'+pageId+' .content').animate({left: 0}, 700, 'jease');
  $('#slider-movable').animate({left:-offset+'px'}, 300, 'jease', function() {
    $(this).css('left',-offset+'px');
    $('.e'+pageId).addClass('current');
    $('.e'+pageId).css('borderTopWidth','7px');
    currentSlide=pageId;
  });
}

function prepareSlides(width,init) {
  if(typeof init =='undefined') {
    init=false;
  }
  if(width<710) {
    width=710;
  }
  $('#slider').width(width);
  var offset=0;
  $('.slide').each(function() {
    // $(this).width(width);
    $(this).css('left',offset+'px');
    $(this).data('offset',offset);
    // $(this).find('.content').width(width-320);
    offset+=width;
  });
  $('#slider-movable').width(offset);
  if(init) {
    $('#slider-movable').css('left','-'+offset+'px');
    goTo(currentSlide);
  }
}

function sendEmailInquiry() {
  $('#request-form-error, #request-form-success, #request-form, #link-submit').fadeOut();
  $.post('/send-email-inquiry/', $('#request-form').serialize()).
      success(function () {
          $('#request-form-success').fadeIn();
      }).
      error(function () {
          $('#request-form-error, #request-form, #link-submit').fadeIn();
      });
}



$(document).ready(function() {
  // $('#slider').css({left:488+'px'});
  var sliderW=$(window).width()-$('#slider').position().left;
  prepareSlides(sliderW,true);
  if(!Modernizr.input.placeholder) {
    $('input.text').each(function() {
      $(this).val($(this).attr('placeholder'));
      $(this).on('keyup', function(e) {
        if($(this).val().length==0) {
          $(this).addClass('empty')
        } else if(e.which>47) {
          if($(this).hasClass('empty')) {
            $(this).val(String.fromCharCode(e.which));
          }
          $(this).removeClass('empty')
        }
      }).on('focusout',function() {
        if($(this).val().length==0) {
          $(this).addClass('empty');
          $(this).val($(this).attr('placeholder'));
        }
      }).on('focusin', function() {
        if($(this).hasClass('empty')) {
          $(this).val('');
        }
      });
    });
  } else {
    $('input.text').on('keyup', function() {
      if($(this).val().length>0) {
        $(this).removeClass('empty');
      } else {
        $(this).addClass('empty');
      }
    });
  }
  $('#link-submit').on('click', function(e) {
    e.preventDefault();
    sendEmailInquiry();
  });

  $(window).on('resize', function() {
    sliderW=$(window).width()-$('#slider').position().left;
    prepareSlides(sliderW);
    goTo(currentSlide);
  });

  $('.slideme').on('click', function(e) {
    e.preventDefault();
    goTo($(this).data('idx'));
  });

// switch to hash denoted slide no when called externally, this is messy
// goTo();

});