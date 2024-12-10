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

    // Decrement counter
    decrementBtn.addEventListener("click", async () => {
        const res = await fetch("/decrement-counter/")
        const data = await res.json()  
        counterValue.textContent = data.value  
    });

    // increment counter
    incrementBtn.addEventListener("click", async () => {      
        const res = await fetch("/increment-counter/")
        const data =  await res.json()
        counterValue.textContent = data.value
    });

});




