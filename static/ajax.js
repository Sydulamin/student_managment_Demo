document.addEventListener("DOMContentLoaded", function () {
    const counterValue = document.getElementById("counter-value");
    const incrementBtn = document.getElementById("increment-btn");
    const decrementBtn = document.getElementById("decrement-btn");

    // Fetch the initial counter value
    fetch("/get-counter/")
        .then(response => response.json())
        .then(data => {
            counterValue.textContent = data.value;
        });

    // Increment counter
    incrementBtn.addEventListener("click", () => {
        fetch("/increment-counter/")
            .then(response => response.json())
            .then(data => {
                counterValue.textContent = data.value;
            });
    });

    // Decrement counter
    decrementBtn.addEventListener("click", () => {
        fetch("/decrement-counter/")
            .then(response => response.json())
            .then(data => {
                counterValue.textContent = data.value;
            });
    });
});
