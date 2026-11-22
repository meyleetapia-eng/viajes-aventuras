CREATE TABLE Customers (
    customer_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) NOT NULL,
    password VARCHAR2(255) NOT NULL,
    phone VARCHAR2(20)
);

CREATE TABLE Packages (
    package_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_cost NUMBER(10, 2) NOT NULL
);

CREATE TABLE Destinations (
    destinations_id NUMBER PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    location VARCHAR2(100) NOT NULL,
    description VARCHAR2(500),
    base_price NUMBER(10, 2) NOT NULL
);

CREATE TABLE Package_destinations (
    package_id NUMBER NOT NULL,
    destinations_id NUMBER NOT NULL,
    PRIMARY KEY (package_id, destinations_id),
    FOREIGN KEY (package_id) REFERENCES Packages(package_id),
    FOREIGN KEY (destinations_id) REFERENCES Destinations(destinations_id)
);

CREATE TABLE Bookings (
    bookings_id NUMBER PRIMARY KEY,
    customer_id NUMBER NOT NULL,
    package_id NUMBER NOT NULL,
    bookings_date DATE NOT NULL,
    status VARCHAR2(50) NOT NULL,
    amount_paid NUMBER(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (package_id) REFERENCES Packages(package_id)
);