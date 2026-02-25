
const API_URL = "http://127.0.0.1:8000/api";
    
// =======================
// Завантаження таблиць
// =======================
async function loadData(endpoint, tableId) {
    const tbody = document.getElementById(tableId);
    if (!tbody) return;

    try {
        const response = await fetch(`${API_URL}/${endpoint}`);
        const data = await response.json();

        tbody.innerHTML = '';

        data.forEach(item => {

            let content = '';

            if (endpoint === 'students') {
                content = `
                    <td>${item.name}</td>
                    <td>${item.email}</td>
                    <td>${item.phone}</td>
                `;
            } else if (endpoint === 'courses') {
                content = `
                    <td>${item.course}</td>
                    <td>${item.name}</td>
                    <td>${item.status}</td>
                `;
            }

            tbody.innerHTML += `
                <tr class="user">
                    ${content}
                    <td>
                        <div class="user-action">
                            <a href="edit_user.html?id=${item.id}" class="edit-btn btn green small">
                                <img src="../static/feather.svg" alt="Edit">
                            </a>
                            <button onclick="deleteItem(${item.id}, '${endpoint}')" 
                                    class="remove-btn btn red small" 
                                    style="border:none; cursor:pointer;">
                                <img src="../static/basket.svg" alt="Delete">
                            </button>
                        </div>
                    </td>
                </tr>
            `;
        });

    } catch (e) {
        console.error(e);
    }
}

// =======================
// Видалення
// =======================
async function deleteItem(id, endpoint) {
    if (!confirm("Ви впевнені?")) return;

    let url = '';

    if (endpoint === 'students') {
        url = `${API_URL}/students/delete/${id}`;
    } else if (endpoint === 'courses') {
        url = `${API_URL}/courses/delete/${id}`;
    }

    const response = await fetch(url, { method: 'DELETE' });

    if (response.ok) location.reload();
}

// =======================
// Створення
// =======================
async function handleCreateUser(event) {
    event.preventDefault();

    const data = Object.fromEntries(new FormData(event.target));

    const response = await fetch(`${API_URL}/create_user`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        window.location.href = "index.html",
        window.location.href = "courses.html";
    }
}

// =======================
// Редагування (заповнення)
// =======================
async function fillEditForm() {
    const id = new URLSearchParams(window.location.search).get('id');
    if (!id) return;

    const response = await fetch(`${API_URL}`);
    const users = await response.json();

    const user = users.find(u => u.id == id);

    if (user) {
        for (let key in user) {
            const input = document.querySelector(`[name="${key}"]`);
            if (input) input.value = user[key];
        }
    }
}

// =======================
// Редагування (збереження)
// =======================
async function handleUpdateUser(event) {
    event.preventDefault();

    const id = new URLSearchParams(window.location.search).get('id');
    const data = Object.fromEntries(new FormData(event.target));

    const response = await fetch(`${API_URL}/students_edit/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        window.location.href = "index.html",
        window.location.href = "courses.html";
    }
}