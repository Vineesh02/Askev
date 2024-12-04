import sqlite3

conn = sqlite3.connect('company_services.db')
cursor = conn.cursor()

# Create company_details table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS company_details (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)''')

# Create product_info table
cursor.execute('''CREATE TABLE IF NOT EXISTS product_info (
    id INTEGER PRIMARY KEY,
    about_product TEXT,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES company_details(id)
)''')

# Create product_details table
cursor.execute('''CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    product_image TEXT,
    product_price TEXT,
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

# Create services table
cursor.execute('''CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY,
    service_name TEXT,
    service_description TEXT,
    company_id INTEGER,
    email TEXT,
    phone_number TEXT,
    FOREIGN KEY(company_id) REFERENCES company_details(id)
)''')

conn.commit()
conn.close()
