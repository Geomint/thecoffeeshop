// account navigation js goes here 
const accountNavButton = $('.profile__navigation__link__account');
const orderNavButton = $('.profile__navigation__link__orders');
const accountPanel = $('.profile__dashboard__account');
const ordersPanel = $('.profile__dashboard__orders');
const editProfileTrigger = $('.edit-profile-trigger');
const editProfileClose = $('.edit-profile-close');

accountNavButton.on('click', function(){
    accountPanel.show();
    ordersPanel.hide();
    return false;
});

orderNavButton.on('click', function(){
    accountPanel.hide();
    ordersPanel.show();
    return false;
});

editProfileTrigger.on('click', function(){
    $('#edit-details-form').addClass('profile__dashboard__edit__form__show');
    editProfileTrigger.hide();
    editProfileClose.removeClass('profile__dashboard__edit__close');
    return false;
});

editProfileClose.on('click', function(){
    $('#edit-details-form').removeClass('profile__dashboard__edit__form__show');
    editProfileTrigger.show();
    editProfileClose.addClass('profile__dashboard__edit__close');
    return false;
});