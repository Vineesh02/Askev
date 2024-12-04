import sqlite3

def add_product_description_column():
    conn = sqlite3.connect('company_services.db')
    cursor = conn.cursor()

    # Add the product_description column
    cursor.execute('''
    ALTER TABLE product_details ADD COLUMN product_description TEXT;
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_product_description_column()
