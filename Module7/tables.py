import sqlite3


def setup_database(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    sql_script = """
    CREATE TABLE Product (
        ProductID INTEGER PRIMARY KEY,
        Name TEXT,
        ProductNumber TEXT,
        Color TEXT,
        StandardCost REAL,
        ListPrice REAL,
        Size TEXT,
        Weight REAL,
        CategoryID INTEGER,
        ProductModelID INTEGER,
        SellStartDate TEXT,
        SellEndDate TEXT,
        DiscontinuedDate TEXT,
        ModifiedDate TEXT
    );

    CREATE TABLE Category (
        CategoryID INTEGER PRIMARY KEY,
        ParentCategoryID INTEGER,
        Name TEXT,
        ModifiedDate TEXT
    );

    CREATE TABLE Customer (
        CustomerID INTEGER PRIMARY KEY,
        Title TEXT,
        FirstName TEXT,
        MiddleName TEXT,
        LastName TEXT,
        Suffix TEXT,
        CompanyName TEXT,
        SalesPerson TEXT,
        EmailAddress TEXT,
        Phone TEXT,
        ModifiedDate TEXT
    );

    CREATE TABLE Address (
        AddressID INTEGER PRIMARY KEY,
        AddressLine1 TEXT,
        AddressLine2 TEXT,
        City TEXT,
        StateProvince TEXT,
        PostalCode TEXT,
        ModifiedDate TEXT,
        Country TEXT
    );

    CREATE TABLE CustomerAddress (
        CustomerID INTEGER,
        AddressID INTEGER,
        PRIMARY KEY (CustomerID, AddressID),
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (AddressID) REFERENCES Address(AddressID)
    );

    CREATE TABLE Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        OrderDate TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
    );

    CREATE TABLE OrderDetail (
        OrderDetailID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
    );

    CREATE TABLE ProductModel (
        ProductModelID INTEGER PRIMARY KEY,
        Name TEXT,
        ModifiedDate TEXT
    );
    """

    cursor.executescript(sql_script)
    connection.commit()
    connection.close()
    print(f"Database '{db_name}' and tables created successfully!")


if __name__ == "__main__":
    setup_database("ecommerce.db")
