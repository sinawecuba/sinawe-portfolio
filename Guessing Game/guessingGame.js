// Step 1: Generate a random secret number between 1 and 20
let secret = Math.floor(Math.random() * 20) + 1;

// Step 2: Ask the user to guess, and convert the input to a number in one line
let guess = parseInt(prompt("Please guess the secret number (1-20):"));

// Step 3: Repeat until the guess is correct
while (guess !== secret) {
    // Step 4: Check if guess is too low or too high
    if (guess < secret) {
        alert("Incorrect, too low");
    } else if (guess > secret) {
        alert("Incorrect, too high");
    } else {
        alert("Sorry, incorrect guess.");
    }

    // Ask again
    guess = parseInt(prompt("Please guess again (1-20):"));
}

// Step 5: If correct, show success message
alert("Correct Guess!");
