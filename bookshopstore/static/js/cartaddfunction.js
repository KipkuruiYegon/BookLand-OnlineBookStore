var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var bookId = this.dataset.book;
        var action = this.dataset.action;
        console.log('bookId:', bookId, 'action:', action);

        console.log('USER:', user);
        if (user === 'AnonymousUser') {
            console.log('Not Logged in');
        } else {
            updateUserOrder(bookId, action);
        }
    });
}

function updateUserOrder(bookId, action) {
    console.log('User logged in, sending some data');

    var url = '/updateItem/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'bookId': bookId, 'action': action })
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        console.log('data:', data);
        location.reload();
    });
}

// Add keyboard event listener for quantity input
var quantityInputs = document.getElementsByClassName('quantity');

for (var i = 0; i < quantityInputs.length; i++) {
    quantityInputs[i].addEventListener('input', function () {
        var bookId = this.querySelector('.chg-quantity').dataset.book;
        var action = 'update'; // or any action that corresponds to updating quantity
        var quantity = this.querySelector('.quantity').value;

        console.log('bookId:', bookId, 'action:', action, 'quantity:', quantity);

        console.log('USER:', user);
        if (user === 'AnonymousUser') {
            console.log('Not Logged in');
        } else {
            updateUserOrder(bookId, action, quantity);
        }
    });
}
