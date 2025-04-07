```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Mortgage Loan Application</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .form-section { margin-bottom: 20px; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Car Mortgage Loan Application</h1>
    <form id="loanApplicationForm">
        <div class="form-section">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            <span class="error" id="nameError"></span>
        </div>
        <div class="form-section">
            <label for="income">Annual Income:</label>
            <input type="number" id="income" name="income" required>
            <span class="error" id="incomeError"></span>
        </div>
        <div class="form-section">
            <label for="employment">Employment Details:</label>
            <input type="text" id="employment" name="employment" required>
            <span class="error" id="employmentError"></span>
        </div>
        <div class="form-section">
            <button type="button" onclick="saveProgress()">Save Progress</button>
            <button type="submit">Submit Application</button>
        </div>
        <div id="confirmationMessage"></div>
    </form>
    <script>
        function validateForm() {
            let isValid = true;
            document.querySelectorAll('.error').forEach(e => e.textContent = '');
            if (!document.getElementById('name').value) {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }
            if (!document.getElementById('income').value) {
                document.getElementById('incomeError').textContent = 'Income is required.';
                isValid = false;
            }
            if (!document.getElementById('employment').value) {
                document.getElementById('employmentError').textContent = 'Employment details are required.';
                isValid = false;
            }
            return isValid;
        }

        function saveProgress() {
            localStorage.setItem('loanApplication', JSON.stringify({
                name: document.getElementById('name').value,
                income: document.getElementById('income').value,
                employment: document.getElementById('employment').value
            }));
            alert('Progress saved.');
        }

        document.getElementById('loanApplicationForm').addEventListener('submit', function(event) {
            event.preventDefault();
            if (validateForm()) {
                document.getElementById('confirmationMessage').textContent = 'Application submitted successfully!';
            }
        });

        window.onload = function() {
            const savedData = JSON.parse(localStorage.getItem('loanApplication'));
            if (savedData) {
                document.getElementById('name').value = savedData.name || '';
                document.getElementById('income').value = savedData.income || '';
                document.getElementById('employment').value = savedData.employment || '';
            }
        };
    </script>
</body>
</html>
```