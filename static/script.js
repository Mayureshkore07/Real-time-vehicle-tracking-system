document.getElementById("etaForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let source = document.getElementById("source").value;
    let destination = document.getElementById("destination").value;

    fetch("/calculate", {
        method: "POST",
        body: new URLSearchParams({ source: source, destination: destination }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerText = "Error: " + data.error;
        } else {
            document.getElementById("result").innerText = "Estimated Time: " + data.estimated_time + " minutes";
        }
    });
});
