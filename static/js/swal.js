// sweetalert2

const addToCartButton = $('#add-to-cart');
const cartForm = $('#cart-form');
const editCartQtyButton = $('#edit-qty');
const editCartQtyForm = $('#edit-qty-form');
const checkoutButton = $('#checkout-button')

addToCartButton.click(function (e) {
    e.preventDefault();
    swal({
            title: "Item(s) has been added to the cart",
            icon: "success",
        });
        cartForm.submit()
});

editCartQtyButton.click(function (e) {
    e.preventDefault();
    swal({
            title: "Edit the quantity?",
            text: "This will update the amount of items in your cart",
            icon: "warning",
            buttons: true,
        })
        .then((willEdit) => {
            if (willEdit) {
                swal("Updated the quantity!", {
                    icon: "success",
                });
                editCartQtyForm.submit()
            } else {
                swal({
                    title: "You've kept the quantity the same",
                    icon: "success",
                })
            }
        });
})