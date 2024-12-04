import sqlite3

def create_db():
    conn = sqlite3.connect('company_services.db')
    cursor = conn.cursor()

    # Create company_details table
    cursor.execute('''CREATE TABLE IF NOT EXISTS company_details (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )''')

    # Create product_details table
    cursor.execute('''CREATE TABLE IF NOT EXISTS product_details (
        id INTEGER PRIMARY KEY,
        product_name[] TEXT NOT NULL,
        product_description[] TEXT,
        product_price[] TEXT NOT NULL,
        company_id INTEGER,
        FOREIGN KEY(company_id) REFERENCES company_details(id)
    )''')

    # Create custom_fields table
    cursor.execute('''CREATE TABLE IF NOT EXISTS custom_fields (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        field_name TEXT,
        field_value TEXT,
        FOREIGN KEY(product_id) REFERENCES product_details(id)
    )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
