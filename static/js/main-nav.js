// main-nav js goes here

const searchButton = $('#search-button');

searchButton.on('click', function(){
    $('.search').removeClass('search__hide');
    $('#overlay').addClass('overlay__show');
})