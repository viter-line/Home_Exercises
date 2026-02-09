document
    .getElementById('create-user-form')
    .addEventListener('submit', createUser);

function createUser(e) {
    e.preventDefault();

    const data = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        course: document.getElementById('course').value,
        status: document.getElementById('status').value
    };

    fetch('/api/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        alert('User created');
        window.location.href = 'users.html';
    })
    .catch(err => console.error(err));
}
