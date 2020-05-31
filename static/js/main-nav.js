// main-nav js goes here
const searchButton = $('#search-button');
const overlay = $('#overlay')
const readMore = $("#read-more");
const readLess = $("#read-less");
const descriptionTwo = $("#more-description");
const speed = 200;
const orderForm = $("#payment-form");
const orderPay = $("#pay");

searchButton.on('click', function () {
    $('.search').removeClass('search__hide');
    overlay.addClass('overlay__show');
});

$('.nav-button').on('click', function () {
    overlay.addClass('overlay__show');
    $('html').addClass('open-nav');
});

overlay.on('click', function () {
    $('.search').addClass('search__hide');
    overlay.removeClass('overlay__show');
    $('html').removeClass('open-nav');
});

readMore.on('click', function () {
    descriptionTwo.show(speed);
    readMore.hide(speed);
    return false;
});

readLess.on('click', function () {
    descriptionTwo.hide(speed);
    readMore.show(speed);
    return false;
});

orderPay.on('click', function (){
    orderForm.submit();
    return false;
})