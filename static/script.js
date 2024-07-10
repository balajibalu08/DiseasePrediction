document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('symptomForm');
    const resultDiv = document.getElementById('result');
    const errorDiv = document.getElementById('error');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        
        const symptomsInput = document.getElementById('symptoms').value.trim();
        
        if (!symptomsInput) {
            displayError('Please enter symptoms');
            return;
        }
        
        form.submit();
    });

    function displayError(message) {
        if (errorDiv) {
            errorDiv.textContent = message;
            errorDiv.style.display = 'block';
        } else {
            const errorElement = document.createElement('div');
            errorElement.className = 'error';
            errorElement.id = 'error';
            errorElement.textContent = message;
            form.appendChild(errorElement);
        }
    }
});
