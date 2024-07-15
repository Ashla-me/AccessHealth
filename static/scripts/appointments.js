document.getElementById('appointment-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    const doctor_id = document.getElementById('doctor_id').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    fetch('http://localhost:5000/api/appointments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ doctor_id, date, time }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('message').textContent = 'An error occurred while booking the appointment.';
        });
});

