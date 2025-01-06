import sqlite3

class BaseRepository:
    def __init__(self, db_name="database.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def commit_and_close(self):
        self.connection.commit()
        self.connection.close()

class ProductRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Product (
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
        )''')

    def create(self, product):
        self.cursor.execute('''INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', product)

    def get_all(self):
        self.cursor.execute('SELECT * FROM Product')
        return self.cursor.fetchall()

    def get_by_id(self, product_id):
        self.cursor.execute('SELECT * FROM Product WHERE ProductID = ?', (product_id,))
        return self.cursor.fetchone()

    def update(self, product_id, updated_data):
        self.cursor.execute('''UPDATE Product SET 
            Name=?, ProductNumber=?, Color=?, StandardCost=?, ListPrice=?, Size=?, Weight=?, 
            CategoryID=?, ProductModelID=?, SellStartDate=?, SellEndDate=?, DiscontinuedDate=?, ModifiedDate=? 
            WHERE ProductID = ?''', (*updated_data, product_id))

    def delete_by_id(self, product_id):
        self.cursor.execute('DELETE FROM Product WHERE ProductID = ?', (product_id,))

class CategoryRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Category (
            CategoryID INTEGER PRIMARY KEY,
            ParentCategoryID INTEGER,
            Name TEXT,
            ModifiedDate TEXT
        )''')

    def create(self, category):
        self.cursor.execute('INSERT INTO Category VALUES (?, ?, ?, ?)', category)

    def get_all(self):
        self.cursor.execute('SELECT * FROM Category')
        return self.cursor.fetchall()

    def get_by_id(self, category_id):
        self.cursor.execute('SELECT * FROM Category WHERE CategoryID = ?', (category_id,))
        return self.cursor.fetchone()

    def update(self, category_id, updated_data):
        self.cursor.execute('''UPDATE Category SET 
            ParentCategoryID=?, Name=?, ModifiedDate=? 
            WHERE CategoryID = ?''', (*updated_data, category_id))

    def delete_by_id(self, category_id):
        self.cursor.execute('DELETE FROM Category WHERE CategoryID = ?', (category_id,))

class CustomerRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
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
        )''')

    def create(self, customer):
        self.cursor.execute('INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', customer)

    def get_all(self):
        self.cursor.execute('SELECT * FROM Customer')
        return self.cursor.fetchall()

    def get_by_id(self, customer_id):
        self.cursor.execute('SELECT * FROM Customer WHERE CustomerID = ?', (customer_id,))
        return self.cursor.fetchone()

    def update(self, customer_id, updated_data):
        self.cursor.execute('''UPDATE Customer SET 
            Title=?, FirstName=?, MiddleName=?, LastName=?, Suffix=?, CompanyName=?, SalesPerson=?, 
            EmailAddress=?, Phone=?, ModifiedDate=? 
            WHERE CustomerID = ?''', (*updated_data, customer_id))

    def delete_by_id(self, customer_id):
        self.cursor.execute('DELETE FROM Customer WHERE CustomerID = ?', (customer_id,))

class AddressRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Address (
            AddressID INTEGER PRIMARY KEY,
            AddressLine1 TEXT,
            AddressLine2 TEXT,
            City TEXT,
            StateProvince TEXT,
            PostalCode TEXT,
            ModifiedDate TEXT,
            Country TEXT
        )''')

    def create(self, address):
        self.cursor.execute('INSERT INTO Address VALUES (?, ?, ?, ?, ?, ?, ?, ?)', address)

    def get_all(self):
        self.cursor.execute('SELECT * FROM Address')
        return self.cursor.fetchall()

    def get_by_id(self, address_id):
        self.cursor.execute('SELECT * FROM Address WHERE AddressID = ?', (address_id,))
        return self.cursor.fetchone()

    def update(self, address_id, updated_data):
        self.cursor.execute('''UPDATE Address SET 
            AddressLine1=?, AddressLine2=?, City=?, StateProvince=?, PostalCode=?, ModifiedDate=?, Country=? 
            WHERE AddressID = ?''', (*updated_data, address_id))

    def delete_by_id(self, address_id):
        self.cursor.execute('DELETE FROM Address WHERE AddressID = ?', (address_id,))

class CustomerAddressRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS CustomerAddress (
            CustomerAddressID INTEGER PRIMARY KEY,
            CustomerID INTEGER,
            AddressID INTEGER,
            AddressType TEXT,
            ModifiedDate TEXT
        )''')

    def create(self, customer_address):
        self.cursor.execute('INSERT INTO CustomerAddress VALUES (?, ?, ?, ?, ?)', customer_address)

    def get_all(self):
        self.cursor.execute('SELECT * FROM CustomerAddress')
        return self.cursor.fetchall()

    def get_by_id(self, customer_address_id):
        self.cursor.execute('SELECT * FROM CustomerAddress WHERE CustomerAddressID = ?', (customer_address_id,))
        return self.cursor.fetchone()

    def update(self, customer_address_id, updated_data):
        self.cursor.execute('''UPDATE CustomerAddress SET 
            CustomerID=?, AddressID=?, AddressType=?, ModifiedDate=? 
            WHERE CustomerAddressID = ?''', (*updated_data, customer_address_id))

    def delete_by_id(self, customer_address_id):
        self.cursor.execute('DELETE FROM CustomerAddress WHERE CustomerAddressID = ?', (customer_address_id,))

class OrderRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS "Order" (
            OrderID INTEGER PRIMARY KEY,
            OrderNumber INTEGER,
            RevisionNumber INTEGER,
            OrderDate TEXT,
            ShipDate TEXT,
            Status INTEGER,
            OnlineOrderFlag INTEGER,
            PurchaseOrderNumber TEXT,
            AccountNumber TEXT,
            CustomerID INTEGER,
            ShipToAddressID INTEGER,
            BillToAddressID INTEGER,
            ShipMethod TEXT,
            CreditCardApprovalCode TEXT,
            SubTotal REAL,
            TaxAmt REAL,
            Freight REAL,
            TotalDue REAL,
            Comment TEXT,
            ModifiedDate TEXT
        )''')

    def create(self, order):
        self.cursor.execute('INSERT INTO "Order" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', order)

    def get_all(self):
        self.cursor.execute('SELECT * FROM "Order"')
        return self.cursor.fetchall()

    def get_by_id(self, order_id):
        self.cursor.execute('SELECT * FROM "Order" WHERE OrderID = ?', (order_id,))
        return self.cursor.fetchone()

    def update(self, order_id, updated_data):
        self.cursor.execute('''UPDATE "Order" SET 
            OrderNumber=?, RevisionNumber=?, OrderDate=?, ShipDate=?, Status=?, OnlineOrderFlag=?, 
            PurchaseOrderNumber=?, AccountNumber=?, CustomerID=?, ShipToAddressID=?, BillToAddressID=?, 
            ShipMethod=?, CreditCardApprovalCode=?, SubTotal=?, TaxAmt=?, Freight=?, TotalDue=?, Comment=?, ModifiedDate=? 
            WHERE OrderID = ?''', (*updated_data, order_id))

    def delete_by_id(self, order_id):
        self.cursor.execute('DELETE FROM "Order" WHERE OrderID = ?', (order_id,))

class OrderDetailRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS OrderDetail (
            OrderDetailID INTEGER PRIMARY KEY,
            OrderID INTEGER,
            OrderQty INTEGER,
            ProductID INTEGER,
            UnitPrice REAL,
            UnitPriceDiscount REAL,
            LineTotal REAL,
            ModifiedDate TEXT
        )''')

    def create(self, order_detail):
        self.cursor.execute('INSERT INTO OrderDetail VALUES (?, ?, ?, ?, ?, ?, ?, ?)', order_detail)

    def get_all(self):
        self.cursor.execute('SELECT * FROM OrderDetail')
        return self.cursor.fetchall()

    def get_by_id(self, order_detail_id):
        self.cursor.execute('SELECT * FROM OrderDetail WHERE OrderDetailID = ?', (order_detail_id,))
        return self.cursor.fetchone()

    def update(self, order_detail_id, updated_data):
        self.cursor.execute('''UPDATE OrderDetail SET 
            OrderID=?, OrderQty=?, ProductID=?, UnitPrice=?, UnitPriceDiscount=?, LineTotal=?, ModifiedDate=? 
            WHERE OrderDetailID = ?''', (*updated_data, order_detail_id))

    def delete_by_id(self, order_detail_id):
        self.cursor.execute('DELETE FROM OrderDetail WHERE OrderDetailID = ?', (order_detail_id,))

class ProductModelRepository(BaseRepository):
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ProductModel (
            ProductModelID INTEGER PRIMARY KEY,
            Name TEXT,
            CatalogDescription TEXT,
            ModifiedDate TEXT
        )''')

    def create(self, product_model):
        self.cursor.execute('INSERT INTO ProductModel VALUES (?, ?, ?, ?)', product_model)

    def get_all(self):
        self.cursor.execute('SELECT * FROM ProductModel')
        return self.cursor.fetchall()

    def get_by_id(self, product_model_id):
        self.cursor.execute('SELECT * FROM ProductModel WHERE ProductModel = ?', (product_model_id,))
        return self.cursor.fetchone()

    def update(self, product_model_id, updated_data):
        self.cursor.execute('''UPDATE ProductModel SET 
            Name=?, CatalogDescription=?, ModifiedDate=? 
            WHERE ProductModelID = ?''', (*updated_data, product_model_id))

    def delete_by_id(self, product_model_id):
        self.cursor.execute('DELETE FROM ProductModel WHERE ProductModelID = ?', (product_model_id,))


product_repo = ProductRepository()
product_repo.create_table()

product = (1, "Laptop", "yoga", "Silver", 800.0, 1000.0, "Medium", 2.5, 101, 201, "2023-01-01", None, None, "2023-01-02")
product_repo.create(product)

products = product_repo.get_all()
print(products)

updated_product = ("Gaming Laptop", "yoga2", "Black", 1200.0, 1500.0, "Large", 3.0, 101, 202, "2023-01-01", None, None, "2023-06-01")
product_repo.update(1, updated_product)

product_repo.delete_by_id(1)

product_repo.commit_and_close()




