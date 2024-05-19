function processInput() {
    const inputString = document.getElementById('inputString').value;
    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ data: inputString })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').textContent = data.output;
        })
        .catch(error => console.error('Error:', error));
}
