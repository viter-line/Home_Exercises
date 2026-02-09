document.addEventListener('DOMContentLoaded', loadUsers);

function loadUsers() {
    fetch('/api/users')
        .then(res => res.json())
        .then(data => renderUsers(data))
        .catch(err => console.error(err));
}

function renderUsers(users) {
    const tbody = document.querySelector('tbody');
    tbody.innerHTML = '';

    users.forEach(user => {
        const tr = document.createElement('tr');

        tr.innerHTML = `
            <td>${user.name}</td>
            <td>${user.email}</td>
            <td>${user.phone ?? ''}</td>
            <td>
                <div class="user-action">
                    <a href="edit.html?id=${user.id}" class="edit-btn btn green small">
                        ✏️
                    </a>
                    <button class="remove-btn btn red small"
                        onclick="deleteUser(${user.id})">
                        🗑
                    </button>
                </div>
            </td>
        `;

        tbody.appendChild(tr);
    });
}

function deleteUser(id) {
    if (!confirm('Delete user?')) return;

    fetch(`/api/users/${id}`, {
        method: 'DELETE'
    })
    .then(res => res.json())
    .then(() => loadUsers())
    .catch(err => console.error(err));
}
