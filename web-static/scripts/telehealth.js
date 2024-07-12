document.getElementById('telehealth-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    const appointment_id = document.getElementById('appointment_id').value;

    fetch('http://localhost:5000/api/telehealth/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ appointment_id }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                window.location.href = data.url;
            } else {
                document.getElementById('message').textContent = data.message;
            }
        })
        .catch(error => {
            document.getElementById('message').textContent = 'An error occurred while starting the telehealth session.';
        });
});

