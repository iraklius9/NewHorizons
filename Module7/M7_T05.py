import csv
import json
import pickle


class BaseClass:
    def __init__(self):
        self.data = []

    def save_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def load_csv(self, filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            self.data = [row for row in reader]

    def save_json(self, filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(self.data, file)

    def load_json(self, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

    def save_pickle(self, filename):
        with open(filename, mode='wb') as file:
            pickle.dump(self.data, file)

    def load_pickle(self, filename):
        with open(filename, mode='rb') as file:
            self.data = pickle.load(file)

    def __str__(self):
        return str(self.data)


class Address(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [
            ['AddressID', 'AddressLine1', 'AddressLine2', 'City', 'StateProvince', 'PostalCode', 'ModifiedDate',
             'Country']]

    def add_address(self, addressID, addressLine1, addressLine2, city, stateProvince, postalCode, modifiedDate,
                    country):
        self.data.append(
            [addressID, addressLine1, addressLine2, city, stateProvince, postalCode, modifiedDate, country])


class Category(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [['CategoryID', 'ParentCategoryID', 'Name', 'ModifiedDate']]

    def add_category(self, categoryID, parentCategoryID, name, modifiedDate):
        self.data.append([categoryID, parentCategoryID, name, modifiedDate])


class Customer(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [
            ['CustomerID', 'Title', 'FirstName', 'MiddleName', 'LastName', 'Suffix', 'CompanyName', 'SalesPerson',
             'EmailAddress', 'Phone', 'ModifiedDate']]

    def add_customer(self, customerID, title, firstName, middleName, lastName, suffix, companyName, salesPerson,
                     emailAddress, phone, modifiedDate):
        self.data.append(
            [customerID, title, firstName, middleName, lastName, suffix, companyName, salesPerson, emailAddress, phone,
             modifiedDate])


class Order(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [['OrderID', 'OrderNumber', 'RevisionNumber', 'OrderDate', 'ShipDate', 'Status', 'OnlineOrderFlag',
                      'PurchaseOrderNumber', 'AccountNumber', 'CustomerID', 'ShipToAddressID', 'BillToAddressID',
                      'ShipMethod', 'CreditCardApprovalCode', 'SubTotal', 'TaxAmt', 'Freight', 'TotalDue', 'Comment',
                      'ModifiedDate']]

    def add_order(self, orderID, orderNumber, revisionNumber, orderDate, shipDate, status, onlineOrderFlag,
                  purchaseOrderNumber, accountNumber, customerID, shipToAddressID, billToAddressID, shipMethod,
                  creditCardApprovalCode, subTotal, taxAmt, freight, totalDue, comment, modifiedDate):
        self.data.append(
            [orderID, orderNumber, revisionNumber, orderDate, shipDate, status, onlineOrderFlag, purchaseOrderNumber,
             accountNumber, customerID, shipToAddressID, billToAddressID, shipMethod, creditCardApprovalCode, subTotal,
             taxAmt, freight, totalDue, comment, modifiedDate])


class OrderDetail(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [
            ['OrderID', 'OrderDetailID', 'OrderQty', 'ProductID', 'UnitPrice', 'UnitPriceDiscount', 'LineTotal',
             'ModifiedDate']]

    def add_order_detail(self, orderID, orderDetailID, orderQty, productID, unitPrice, unitPriceDiscount, lineTotal,
                         modifiedDate):
        self.data.append(
            [orderID, orderDetailID, orderQty, productID, unitPrice, unitPriceDiscount, lineTotal, modifiedDate])


class Product(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [
            ['ProductID', 'Name', 'ProductNumber', 'Color', 'StandardCost', 'ListPrice', 'Size', 'Weight', 'CategoryID',
             'ProductModelID', 'SellStartDate', 'SellEndDate', 'DiscontinuedDate', 'ModifiedDate']]

    def add_product(self, productID, name, productNumber, color, standardCost, listPrice, size, weight, categoryID,
                    productModelID, sellStartDate, sellEndDate, discontinuedDate, modifiedDate):
        self.data.append(
            [productID, name, productNumber, color, standardCost, listPrice, size, weight, categoryID, productModelID,
             sellStartDate, sellEndDate, discontinuedDate, modifiedDate])


class ProductModel(BaseClass):
    def __init__(self):
        super().__init__()
        self.data = [['ProductModelID', 'Name', 'CatalogDescription', 'ModifiedDate']]

    def add_product_model(self, productModelID, name, catalogDescription, modifiedDate):
        self.data.append([productModelID, name, catalogDescription, modifiedDate])


address = Address()
address.add_address(1, "1 kutaisi st", "Apt 4", "Tbilisi", "Tbilisi", "1234", "2025-01-06", "Georgia")

category = Category()
category.add_category(1, None, "Engineering", "2025-01-06")

customer = Customer()
customer.add_customer(1, None, "Irakli", None, "Meparishvili", None, "CU", "someone", "irakli.meparishvili@gmail.com",
                      "599-27-77-78", "2025-01-06")

product = Product()
product.add_product(1, "Laptop", "Lenovo", "Black", 750.00, 700.00, "Medium", 2.1, 1, 1, "2025-01-01", None, None,
                    "2025-01-06")

product_model = ProductModel()
product_model.add_product_model(1, "Yoga", "Gaming laptop model", "2025-01-06")

order = Order()
order.add_order(1, 1001, 1, "2025-01-05", "2025-01-06", 5, 1, "xO123", "AC1597", 1, 1, 1, "Air", "CC1111", 1000.00,
                80.00, 20.00, 1100.00, None, "2025-01-06")

order_detail = OrderDetail()
order_detail.add_order_detail(1001, 1, 2, 1, 700.00, 0.10, 1260.00, "2025-01-06")

address.save_csv("addresses.csv")
category.save_json("categories.json")
customer.save_pickle("customers.pkl")

loaded_address = Address()
loaded_address.load_csv("addresses.csv")
print("Loaded Addresses:", loaded_address)

loaded_category = Category()
loaded_category.load_json("categories.json")
print("Loaded Categories:", loaded_category)

loaded_customer = Customer()
loaded_customer.load_pickle("customers.pkl")
print("Loaded Customers:", loaded_customer)
