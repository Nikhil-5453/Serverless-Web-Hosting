document.getElementById('contactForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const city = document.getElementById('city').value;

    const response = await fetch('https://1kk2u6dt3l.execute-api.us-east-1.amazonaws.com/prod/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, city })
    });

    const result = await response.json();
    alert(result);
});
