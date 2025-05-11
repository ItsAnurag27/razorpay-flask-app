from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return "✅ Razorpay Flask backend is live with all required policy pages and test payment page!"

@app.route("/privacy")
def privacy():
    return send_from_directory("static", "privacy.html")

@app.route("/terms")
def terms():
    return send_from_directory("static", "terms.html")

@app.route("/shipping")
def shipping():
    return send_from_directory("static", "shipping.html")

@app.route("/contact")
def contact():
    return send_from_directory("static", "contact.html")

@app.route("/refunds")
def refunds():
    return send_from_directory("static", "refunds.html")

@app.route("/test-payment")
def test_payment():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Razorpay Payment</title>
        <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
    </head>
    <body style='font-family: sans-serif; padding: 40px;'>
        <h2>🧪 Razorpay Test Payment Page</h2>
        <p>This page is for Razorpay verification. You can initiate a test payment using the button below.</p>
        <button id='rzp-button'>Pay ₹1</button>

        <script>
        var options = {
            "key": "rzp_test_YourApiKeyHere",  // Replace this with your Razorpay Test API Key
            "amount": "100",
            "currency": "INR",
            "name": "Test Company",
            "description": "Test Transaction",
            "handler": function (response){
                alert("Payment successful. Payment ID: " + response.razorpay_payment_id);
            },
            "prefill": {
                "name": "Test User",
                "email": "test@example.com",
                "contact": "9000090000"
            },
            "theme": {
                "color": "#3399cc"
            }
        };

        var rzp = new Razorpay(options);
        document.getElementById('rzp-button').onclick = function(e){
            rzp.open();
            e.preventDefault();
        }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
