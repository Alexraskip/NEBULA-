$(document).ready(function() {
    $('.js-example-basic-single').select2();
    
    fetch('/api/students')
    .then(response => response.json())
    .then(data => {
        const studentsSelect = $('#names');
        const cohortsSelect = $('#cohorts');

        data.students.forEach(name => {
            studentsSelect.append(new Option(name, name, true, true)).trigger('change');
        });

        data.cohorts.forEach(cohort => {
            cohortsSelect.append(new Option(cohort, cohort, true, true)).trigger('change');
        });
    })
    .catch(error => console.log(error));
});
