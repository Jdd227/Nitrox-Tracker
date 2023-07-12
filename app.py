from flask import Flask, request, render_template
import csv
import os

directory = "data"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    date = request.form.get('date')
    diver_name = request.form.get('diver_name')
    tank_serial_number = request.form.get('tank_serial_number')
    nitrox_percentage = request.form.get('nitrox_percentage')
    approval_status = request.form.get('approval_status')
    diver_signature = request.form.get('diver_signature')

    # Save the form data to CSV
    with open(os.path.join(directory, 'nitrox_signout.csv'), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, diver_name, tank_serial_number, nitrox_percentage, approval_status, diver_signature])

    # Display the signatures in the response
    return f"Form submitted successfully<br><br>Signature: {diver_signature}"

if __name__ == '__main__':
    app.run()
