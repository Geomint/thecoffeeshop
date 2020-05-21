// account navigation
const accountNavButton = $('.profile__navigation__link__account');
const orderNavButton = $('.profile__navigation__link__orders');
const productNavButton = $('.profile__navigation__link__product-upload');
const accountPanel = $('.profile__dashboard__account');
const ordersPanel = $('.profile__dashboard__orders');
const productPanel = $('.profile__dashboard__product');

accountNavButton.on('click', function(){
    accountPanel.show();
    ordersPanel.hide();
    productPanel.hide();
})

orderNavButton.on('click', function(){
    accountPanel.hide();
    ordersPanel.show();
    productPanel.hide();
})

productNavButton.on('click', function(){
    accountPanel.hide();
    ordersPanel.hide();
    productPanel.show();
})