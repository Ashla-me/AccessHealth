document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:5000/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.token) {
                localStorage.setItem('token', data.token);
                window.location.href = 'doctors.html
document.getElementById('register-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    fetch('http://localhost:5000/api/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password, role }),
    })
        .then(response => response.json())
        .then(data => {
            const messageElement = document.getElementById('message');
            if (data.message) {
                messageElement.textContent = data.message;
            } else {
                messageElement.textContent = 'Registration successful! You can now login.';
            }
        })
        .catch(error => {
            document.getElementById('message').textContent = 'An error occurred. Please try again.';
        });
});

document.getElementById('logout').addEventListener('click', function () {
    localStorage.removeItem('token');
});

