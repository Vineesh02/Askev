from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route for Company Details Form
@app.route('/', methods=['GET', 'POST'])
def company_details():
    if request.method == 'POST':
        company_name = request.form['company_name']
        company_description = request.form['company_description']

        conn = sqlite3.connect('company_services.db')
        cursor = conn.cursor()

        # Save company details
        cursor.execute('INSERT INTO company_details (name, description) VALUES (?, ?)', 
                       (company_name, company_description))
        company_id = cursor.lastrowid
        conn.commit()

        # Redirect to the product details page
        return redirect(url_for('product_details', company_id=company_id))

    return render_template('company_details.html')

# Route for Product Details Form
@app.route('/product-details/<int:company_id>', methods=['GET', 'POST'])
def product_details(company_id):
    if request.method == 'POST':
        # Get all the product details from the form
        product_names = request.form.getlist('product_name[]')
        product_descriptions = request.form.getlist('product_description[]')
        product_prices = request.form.getlist('product_price[]')
        custom_field_names = request.form.getlist('custom_field_name[][]')
        custom_field_values = request.form.getlist('custom_field_value[][]')

        conn = sqlite3.connect('company_services.db')
        cursor = conn.cursor()

        # Iterate over all products and save them
        for i in range(len(product_names)):
            cursor.execute('''INSERT INTO product_details (product_name, product_description, product_price, company_id)
                            VALUES (?, ?, ?, ?)''', 
                            (product_names[i], product_descriptions[i], product_prices[i], company_id))
            product_id = cursor.lastrowid

            # Save custom fields for each product
            for j in range(len(custom_field_names)):
                if custom_field_names[j] and custom_field_values[j]:
                    cursor.execute('''INSERT INTO custom_fields (product_id, field_name, field_value)
                                    VALUES (?, ?, ?)''', 
                                    (product_id, custom_field_names[j], custom_field_values[j]))

            conn.commit()

        # Redirect back to the company details page
        return redirect(url_for('company_details'))

    return render_template('product_details.html', company_id=company_id)

if __name__ == '__main__':
    app.run(debug=True)
