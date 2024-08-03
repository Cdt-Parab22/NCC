import http.server
import socketserver
import json
import qrcode

# Port number to run the server on
PORT = 8000


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expense Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Expense Tracker</h1>
        <form id="expenseForm">
            <label for="item">Item:</label>
            <input type="text" id="item" name="item" required><br>
            <label for="amount">Amount (INR):</label>
            <input type="number" id="amount" name="amount" required><br>
            <label for="category">Category:</label>
            <select id="category" name="category">
                <option value="gold">Gold</option>
                <option value="electronics">Electronics</option>
                <option value="food">Food</option>
            </select><br>
            <button type="button" onclick="submitExpense()">Add Expense</button>
        </form>
        <div id="expenseSummary"></div>
    </div>

    <script>
        function submitExpense() {
            var form = document.getElementById('expenseForm');
            var formData = new FormData(form);
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/add-expense', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    form.reset();
                    updateExpenseSummary(xhr.responseText);
                }
            };
            xhr.send(JSON.stringify(Object.fromEntries(formData)));
        }

        function updateExpenseSummary(summary) {
            document.getElementById('expenseSummary').innerHTML = summary;
        }
    </script>
</body>
</html>
"""

# Store expenses
expenses = []

# Handle HTTP requests
class ExpenseHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode())
        elif self.path == '/get-expenses':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(expenses).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())
        
        if self.path == '/add-expense':
            item = data['item']
            amount = int(data['amount'])
            category = data['category']
            
            # Calculate GST based on category
            gst_percent = get_gst_percent(category)
            total_amount = amount + (amount * gst_percent / 100)
            
            expenses.append({
                'item': item,
                'amount': amount,
                'category': category,
                'total_amount': total_amount
            })
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Expense added successfully".encode())

def get_gst_percent(category):
    gst_rates = {
        'gold': 3,
        'electronics': 18,
        'food': 5
    }
    return gst_rates.get(category, 0)

# Create QR Code for expenses
def generate_qr_code():
    expenses_data = json.dumps(expenses)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(expenses_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("expenses_qr.png")

# Run the server
with socketserver.TCPServer(("", PORT), ExpenseHandler) as httpd:
    print(f"Expense Tracker server running on port {PORT}")
    httpd.serve_forever()
