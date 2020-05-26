// main-nav js goes here

const searchButton = $('#search-button');
const overlay = $('#overlay')

searchButton.on('click', function(){
    $('.search').removeClass('search__hide');
    overlay.addClass('overlay__show');
});

$('.nav-button').on('click', function () {
    overlay.addClass('overlay__show');   
    $('html').addClass('open-nav');
});

overlay.on('click', function(){
    $('.search').addClass('search__hide');
    overlay.removeClass('overlay__show');
    $('html').removeClass('open-nav');
})


