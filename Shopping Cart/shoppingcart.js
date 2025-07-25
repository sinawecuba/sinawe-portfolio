// Item identifiers
var nums = [1, 2, 3, 4, 5, 6, 7, 8]; // Item numbers
var items = ["Eggs", "Milk", "Bread", "Chicken", "Apples", "Rice", "Spinach", "Peanut butter"]; // Item names
var prices = [7.5, 9.5, 8.5, 7.5, 10, 4, 5.5, 9]; // Prices for each item

// Tracking user selections
var quantities = [0, 0, 0, 0, 0, 0, 0, 0]; // Quantity of each item selected
var totals = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]; // Total price for each item
var totalOrderAmt = 0; // Total amount of the entire order

// Called when user clicks 'Add' button
function add_selection(x) {
    console.log(x); // Log index of added item
    quantities[x] += 1; // Increase quantity
    totals[x] = prices[x] * quantities[x]; // Update total for item
    totalOrderAmt += prices[x]; // Increase overall total

    display_all(); // Refresh table display
}

// Called when user clicks 'Remove' button
function remove_selection(x) {
    if (quantities[x] > 0) { // Only remove if quantity > 0
        quantities[x] -= 1; // Decrease quantity
        totals[x] = prices[x] * quantities[x]; // Update item total
        totalOrderAmt -= prices[x]; // Decrease overall total

        display_all(); // Refresh table
    }
}

// Display shopping cart in HTML
function display_all() {
    var myTable = "<table><th style='width: 100px; color: Orange; text-align: right;'>Num</th>";
    myTable += "<th style='width: 100px; color: Navy; text-align: right;'>Item</th>";
    myTable += "<th style='width: 100px; color: Navy; text-align: right;'>Price</th>";
    myTable += "<th style='width: 100px; color: Navy; text-align: right;'>Quantity</th>";
    myTable += "<th style='width: 100px; color: Navy; text-align: right;'>Total</th>";
    myTable += "<th style='width: 100px; color: Green; text-align: right;'>Add</th>";
    myTable += "<th style='width: 100px; color: Red; text-align: right;'>Remove</th>";

    // Loop through each item and display row
    for (var i = 0; i < items.length; i++) {
        myTable += "<tr><td style='width: 100px; text-align: right;'>" + nums[i] + "</td>";
        myTable += "<td style='width: 100px; text-align: right;'>" + items[i] + "</td>";
        myTable += "<td style='width: 100px; text-align: right;'>" + prices[i] + "</td>";
        myTable += "<td style='width: 100px; text-align: right;'>" + quantities[i] + "</td>";
        myTable += "<td style='width: 100px; text-align: right;'>" + totals[i].toFixed(2) + "</td>";
        myTable += "<td><button onclick='add_selection(" + i + ")'>Add</button></td>";
        myTable += "<td><button onclick='remove_selection(" + i + ")'>Remove</button></td></tr>";
    }

    myTable += "</table>";

    // Add the checkout button and total display container
    myTable += "<br/><button onclick='checkout()'>Checkout</button>";
    myTable += "<p id='checkoutTotal'></p>"; // Placeholder for total amount

    // Output the full table to the page
    document.getElementById("demo").innerHTML = myTable;
}

// Called when user clicks 'Checkout' button
function checkout() {
    document.getElementById("checkoutTotal").innerHTML = "<strong>Total Order Amount: R" + totalOrderAmt.toFixed(2) + "</strong>";
}

// Initialize table on page load
window.onload = function () {
    display_all();
}
