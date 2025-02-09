document.getElementById('reportForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let title = document.getElementById('title').value;
    let description = document.getElementById('description').value;

    // Send disaster report to Django API
    fetch('http://127.0.0.1:8000/api/report/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            description: description
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('statusMessage').innerText = "Report Submitted Successfully!";
    })
    .catch(error => {
        document.getElementById('statusMessage').innerText = "Error Submitting Report!";
    });
});
