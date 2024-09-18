function submitCode() {
    let userCode = document.getElementById('code-input').value;

    // Send user code to the back-end for evaluation
    fetch('/run_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: userCode }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('code-output').innerText = data.output;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
