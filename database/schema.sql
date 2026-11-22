CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS Packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    total_cost REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS Destinations (
    destinations_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT,
    base_price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS Package_destinations (
    package_id INTEGER NOT NULL,
    destinations_id INTEGER NOT NULL,
    PRIMARY KEY (package_id, destinations_id),
    FOREIGN KEY (package_id) REFERENCES Packages(package_id),
    FOREIGN KEY (destinations_id) REFERENCES Destinations(destinations_id)
);

CREATE TABLE IF NOT EXISTS Bookings (
    bookings_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    bookings_date TEXT NOT NULL,
    status TEXT NOT NULL,
    amount_paid REAL NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES Packages(package_id)
);