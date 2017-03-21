var Prices = {
    Castle: 100,
    Sports: 100,
    Princess: 100,
    Dolphin: 175,
    Elephant: 175,
    Slide: 175,
};

function addToCart(bouncer_name) {
    var price = Number(Prices[bouncer_name]);
    var total = Number($("#total").text());
    total += price;
    $("#total").text(total);
    var quan_id = "#" + bouncer_name;
    var quantity = Number($(quan_id).text());
    if (quantity >= 0) {
        quantity++;
        $(quan_id).text(quantity);
        alert(bouncer_name + ' Bouncer was added to the cart for $' + price);
    } else {
        alert("Sorry that item is no longer available");
    }
};

function removeFromCart(bouncer_name) {
    var price = Number(Prices[bouncer_name]);
    var total = Number($("#total").text());
    var quan_id = "#" + bouncer_name;
    var quantity = Number($(quan_id).text());
    if (quantity >= 1) {
      total -= price;
      $("#total").text(total);
      quantity--;
      $(quan_id).text(quantity);
      alert(bouncer_name + ' Bouncer was removed from the cart');
    } else {
        alert("Sorry that item is no longer available");
    }
};
