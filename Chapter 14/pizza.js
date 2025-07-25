// listen for button clicks
document.getElementById("placeOrder").addEventListener("click", placeOrder); // Call placeOrder when button is clicked

/**
 * Gets form values, calculates prices, and displays the result
 */
function placeOrder() {
    // Get form input values
    var numPizzas = document.getElementById("numPizzas").value;         // Number of pizzas
    var typePizza = document.getElementById("typePizza").value;         // Type of pizza selected
    var deliveryCity = document.getElementById("deliveryCity").value;   // Delivery location
    var birthday = document.getElementById("birthday").value;           // Is it the user's birthday?

    // Calculate the base price of the pizzas
    var orderPrice = calculatePrice(numPizzas, typePizza);

    // Calculate the delivery fee
    var deliveryPrice = calculateDelivery(orderPrice, deliveryCity, birthday);

    // Start building the output message
    var theOutput = "<p>Thank you for your order.</p>";

    // Show free delivery message if applicable
    if (deliveryPrice === 0) {
        theOutput += "<p>You get free delivery!</p>";
    } else {
        theOutput += "<p>Your delivery cost is: $" + deliveryPrice + "</p>";
    }

    // Show total price (pizza + delivery)
    theOutput += "<p>Your total is: $" + (orderPrice + deliveryPrice) + "</p>";

    // Display output in the browser
    document.getElementById("displayTotal").innerHTML = theOutput;
}

/**
 * Calculates the pizza price based on type and quantity
 */
function calculatePrice(numPizzas, typePizza) {
    var orderPrice = Number(numPizzas) * 10; // Base price: $10 per pizza
    var extraCharge = 0;

    // Add $2 extra per pizza if it's a "supreme"
    if (typePizza === "supreme") {
        extraCharge = Number(numPizzas) * 2;
    } else if(typePizza === "bacon") {
        extraCharge = Number(numPizzas) * 5;
    }
    orderPrice += extraCharge;
    return orderPrice;


}
/**
 * Calculates the delivery price
 */
function calculateDelivery(orderPrice, deliveryCity, birthday) {
    var deliveryPrice = 0;

    // Free delivery if:
    // - Delivering to Stockholm AND order is over $10
    // - OR it's the user's birthday
    if (((deliveryCity === "Stockholm") && (orderPrice > 10)) || (birthday === "yes")) {
        deliveryPrice = 0;
    } else {
        deliveryPrice = 5; // Otherwise, delivery costs $5
    }

    return deliveryPrice; // Return final delivery fee
}
