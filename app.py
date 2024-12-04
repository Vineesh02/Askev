from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder for uploaded images

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Route to Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route for Company Details Form
@app.route('/company-details', methods=['GET', 'POST'])
def company_details():
    if request.method == 'POST':
        company_name = request.form['company_name']
        company_description = request.form['company_description']
        product_file = request.files['product_file']

        conn = sqlite3.connect('company_services.db')
        cursor = conn.cursor()

        # Save company details
        cursor.execute('INSERT INTO company_details (name, description) VALUES (?, ?)', 
                       (company_name, company_description))
        company_id = cursor.lastrowid
        conn.commit()

        # Process CSV file
        if product_file:
            csv_data = csv.reader(product_file.stream.read().decode("utf-8").splitlines())
            for row in csv_data:
                cursor.execute('INSERT INTO product_info (about_product, company_id) VALUES (?, ?)', 
                               (row[0], company_id))
            conn.commit()

        # Process dynamically added product details
        product_names = request.form.getlist('product_name[]')
        product_prices = request.form.getlist('product_price[]')
        custom_field_names = request.form.getlist('custom_field_name[]')
        custom_field_values = request.form.getlist('custom_field_value[]')

        product_images = request.files.getlist('product_image[]')

        for i, name in enumerate(product_names):
            # Save product details
            image = product_images[i]
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)

            cursor.execute('INSERT INTO product_details (product_name, product_image, product_price, company_id) VALUES (?, ?, ?, ?)',
                           (name, image_path, product_prices[i], company_id))
            product_id = cursor.lastrowid
            conn.commit()

            # Save custom fields
            for j in range(len(custom_field_names)):
                if custom_field_names[j] and custom_field_values[j]:
                    cursor.execute('INSERT INTO custom_fields (product_id, field_name, field_value) VALUES (?, ?, ?)',
                                   (product_id, custom_field_names[j], custom_field_values[j]))
                    conn.commit()

        return redirect(url_for('index'))  # Redirect to the index page

    return render_template('company_details.html')

# Route for Service Details Form
@app.route('/service-details', methods=['GET','POST'])
def service_details():
    if request.method == 'POST':
        company_name = request.form['company_name']
        company_description = request.form['company_description']
        service_name = request.form['service_name']
        service_description = request.form['service_description']
        email = request.form['email']
        phone_number = request.form['phone_number']

        conn = sqlite3.connect('company_services.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO company_details (name, description) VALUES (?, ?)', 
                       (company_name, company_description))
        company_id = cursor.lastrowid
        conn.commit()

        cursor.execute('INSERT INTO services (service_name, service_description, company_id, email, phone_number) VALUES (?, ?, ?, ?, ?)',
                       (service_name, service_description, company_id, email, phone_number))
        conn.commit()

        return redirect(url_for('index'))  # Redirect to the index page

    return render_template('service_details.html')

if __name__ == '__main__':
    app.run(debug=True)
