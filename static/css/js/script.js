// script.js
document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/students')
    .then(response => response.json())
    .then(names => {
        const select = document.getElementById('names');
        names.forEach(name => {
            const option = document.createElement('option');
            option.text = name;
            select.appendChild(option);
        });
    })
    .catch(error => console.log(error));
});
