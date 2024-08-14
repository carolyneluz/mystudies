// scripts/form.js
function validateForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const age = document.getElementById('age').value;

    if (!name || !email || !age) {
        alert('Por favor, preencha todos os campos.');
        return false;
    }

    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const formData = {
        name: urlParams.get('name'),
        email: urlParams.get('email'),
        age: urlParams.get('age'),
    };

    if (formData.name && formData.email && formData.age) {
        const formDataDiv = document.getElementById('formData');
        formDataDiv.innerHTML = `
            <p><strong>Nome:</strong> ${formData.name}</p>
            <p><strong>Email:</strong> ${formData.email}</p>
            <p><strong>Idade:</strong> ${formData.age}</p>
        `;
    }
});
