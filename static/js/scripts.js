// static/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('id_password1');
    const passwordConfirmInput = document.getElementById('id_password2');
    const passwordMessage = document.getElementById('password-message');
    const form = document.querySelector('form');

    function validatePassword() {
        if (passwordInput.value !== passwordConfirmInput.value) {
            passwordMessage.textContent = 'Passwords do not match';
            passwordMessage.classList.remove('success');
            passwordMessage.classList.add('error');
            passwordMessage.style.display = 'block';
            passwordConfirmInput.setCustomValidity('Passwords do not match');
        } else {
            passwordMessage.textContent = 'Passwords match';
            passwordMessage.classList.remove('error');
            passwordMessage.classList.add('success');
            passwordMessage.style.display = 'block';
            passwordConfirmInput.setCustomValidity('');
        }
    }

    passwordInput.addEventListener('input', validatePassword);
    passwordConfirmInput.addEventListener('input', validatePassword);

    form.addEventListener('submit', function(event) {
        validatePassword();
        if (!form.checkValidity()) {
            event.preventDefault();
        }
    });
});
