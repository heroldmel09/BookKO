var updatecart = document.getElementsByClassName("update_cart")


for (var i = 0; i < updatecart.length; i++) {
    updatecart[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("your data is add", " productid: ", productId, " action: ", action)
        console.log("hello user:", user)
        if (user === "AnonymousUser") {
            console.log("not log in ")
        } else {
            update_OrderCart(productId, action)
        }
    })
}

function update_OrderCart(product_id, action) {
    console.log("user autheticated the data will send data to db")

    var url = "/Addcart/"

    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

        },
        body: JSON.stringify({ 'productID': product_id, 'action': action })
    })
        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:', data)
        })


}