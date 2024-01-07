var myCursor = $('.myCursor')

function moveMyCursor(e){

    var outerRing = myCursor.find('.outerRing')
    var innerRing = myCursor.find('.innerRing')

    gsap.to(outerRing, 0.6, {
        css: {
        left: e.pageX - outerRing.outerWidth()/2,
        top:  e.pageY - outerRing.outerHeight()/2
        }
    });

    gsap.to(innerRing, 0.4, {
        css: {
        left: e.pageX - innerRing.outerWidth()/2,
        top:  e.pageY - innerRing.outerHeight()/2        
        }
    });
}

$(window).on('mousemove', moveMyCursor)
$(window).on('scroll', moveMyCursor)

$(window).on('mousedown',   () => myCursor.addClass('click') )
$(window).on('mouseup',     () => myCursor.removeClass('click') )

$('.hoverMe').on('mouseenter', (e) => {
    console.log('in' ,e.target)
    myCursor.addClass('hover')
    myCursor.find('.text').text($(e.target).text())
});

$('.hoverMe').on('mouseleave', (e) => {
    myCursor.removeClass('hover')
    myCursor.find('.text').text('')
});