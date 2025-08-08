from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# This route displays the fake login page
@app.route('/')
def login():
    return render_template('login.html')

# This route handles the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the email from the form.
    email = request.form['email']
    # IMPORTANT: We are NOT saving or using the password for anything.
    password = request.form['password']

    # Log the event to the console (or a file).
    timestamp = datetime.datetime.now()
    print(f"[{timestamp}] - Form submitted by: {email}")

    # Redirect the user to the "you've been phished" page.
    return redirect(url_for('caught'))

# This route shows the educational "gotcha" page
@app.route('/caught')
def caught():
    return """
    <h1>This Was a Simulated Phishing Test!</h1>
    <p>If this were a real attack, your credentials would have been stolen.</p>
    <h2>Here's what to look for:</h2>
    <ul>
        <li>Is the sender's email address unfamiliar?</li>
        <li>Does the email create a sense of urgency?</li>
        <li>Hover over links before you click to see the real destination URL.</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)