document.addEventListener('DOMContentLoaded', function () {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = 'login.html';
        return;
    }

    fetch('http://localhost:5000/api/doctors', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
        .then(response => response.json())
        .then(data => {
            const doctorsList = document.getElementById('doctors-list');
            data.forEach(doctor => {
                const listItem = document.createElement('li');
                listItem.textContent = `Dr. ${doctor.name} - ${doctor.specialty}`;
                doctorsList.appendChild(listItem);
            });
        })
        .catch(error => {
            document.getElementById('message').textContent = 'An error occurred while fetching doctors.';
        });
});

