<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Expense Tracker</h1>

        <div class="expense-form">
            <label for="amount">Amount (₹):</label>
            <input type="text" id="amount" placeholder="Enter amount">

            <label for="category">Category:</label>
            <input type="text" id="category" placeholder="Enter category">

            <button onclick="addExpense()">Add Expense</button>
        </div>

        <div class="expense-list">
            <h2>Expenses</h2>
            <ul id="expense-list"></ul>
        </div>

        <div class="qr-code">
            <h2>QR Code</h2>
            <img id="qr-img" src="placeholder.jpg" alt="QR Code">
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
