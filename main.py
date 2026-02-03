from flask import Flask, render_template_string

app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template_string("""
    <h1>MailBud</h1>
    <p>MailBud is an Android application.</p>
    <p>Contact: gauravjoshi3140@gmail.com</p>
    """)

@app.route("/privacy")
def privacy():
    return render_template_string("""
    <h1>Privacy Policy</h1>
    <p>We use Google Sign-In to authenticate users.</p>
    <p>We store your email and name for login purposes.</p>
    <p>Contact: gauravjoshi3140@gmail.com</p>
    """)

@app.route("/terms")
def terms():
    return render_template_string("""
    <h1>Terms of Service</h1>
    <p>This app is provided as-is.</p>
    <p>We may suspend accounts for abuse.</p>
    """)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

